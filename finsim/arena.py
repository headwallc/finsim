from finsim.investment import Investment
from finsim.simulation import simulate_gain_matrix, calculate_return_distribution


class Arena:

    def __init__(self):
        self.investments = []
        self.returns = {}

    def add_investment(self, investment: Investment):
        self.investments.append(investment)

    def simulate(self, k=20, N=10000):
        # ensure same simulation matrix per gains pool
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
        for i in self.returns:
            print(i)
            print(self.returns[i].get_std_quantiles())
