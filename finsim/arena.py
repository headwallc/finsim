from finsim.investment import Investment
from finsim.simulation import simulate_gain_matrix, calculate_return_distribution


class Arena:

    def __init__(self):
        self.k = 20
        self.N = 10000
        self.investments = []
        self.returns = {}

    def add_investment(self, investment: Investment):
        self.investments.append(investment)

    def simulate(self, k=20, N=10000):
        self.k = k
        self.N = N

        # use one simulated matrix per gains pool
        gains = {}
        for i in self.investments:
            if i.gains.name not in gains:
                gains[i.gains.name] = {
                    "gains": i.gains,
                    "sim": None
                }

        # simulate gains
        for g in gains:
            gains[g]["sim"] = simulate_gain_matrix(gains[g]["gains"].gains, k=k, N=N)

        # calculate returns
        self.returns = {}
        for i in self.investments:
            sim = gains[i.gains.name]["sim"]
            self.returns[i] = calculate_return_distribution(sim, i.product)

    def get_returns(self):
        return self.returns

    def print_results(self):
        print(f"Simulation results ({self.k} years, {self.N} simulations):\n")
        for i in self.returns:
            print(i)
            qts = self.returns[i].get_quantiles_5_50_95()
            qts_gain = [int((x-1) * 100) for x in qts]
            annual_pct = [round(x, 2) for x in self.returns[i].get_gain_per_annum_5_50_95(self.k)]
            print(f"95% chance: {qts_gain[0]}% gains, i.e. {annual_pct[0]}% p.a.")
            print(f"50% chance: {qts_gain[1]}% gains, i.e. {annual_pct[1]}% p.a.")
            print(f" 5% chance: {qts_gain[2]}% gains, i.e. {annual_pct[2]}% p.a.")
            print()
