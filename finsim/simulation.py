import math
import random
import numpy as np

from finsim.product import FinancialProduct


def simulate_gains(pool, k=20):
    """
    Simulate k random gains from provided gain pool.
    :param pool: list of annual gains
    :param k: number of years simulated
    :return: list of k gains
    """
    return [random.choice(pool) for x in [None] * k]


def simulate_gain_matrix(pool, k=20, N=1000):
    """
    Bootstrap N random gain vectors of length k from provided gain pool.
    :param pool: list of gains
    :param k: years simulated
    :param N: number of simulations
    :return: k x N matrix of gains
    """
    return [simulate_gains(pool, k) for x in [None] * N]


def calculate_return(gains, product: FinancialProduct, capital=1):
    current_capital = capital
    for g in gains:
        step = current_capital * (1 + product.adjusted_gain(g))
        current_capital = step
    return current_capital


def calculate_return_distribution(simulation, product: FinancialProduct, capital=1):
    returns = [calculate_return(run, product, capital) for run in simulation]
    return Distribution(returns)


class Distribution:
    def __init__(self, returns):
        self.returns = returns
        self.distribution = None

    def get_returns(self):
        return self.returns

    def get_distribution(self, bins=100):
        return np.histogram(self.returns, bins=bins)

    def get_pmf(self, bins=100):
        return np.histogram(self.returns, bins=bins, density=True)

    def get_quantile(self, q):
        return np.quantile(self.returns, q)

    def get_gain_per_annum_5_50_95(self, k):
        qts = self.get_quantiles_5_50_95()
        return [(math.pow(x, 1.0/k) - 1) * 100.0 for x in qts]

    def get_quantiles_5_50_95(self):
        return [
            self.get_quantile(0.05),
            self.get_quantile(0.5),
            self.get_quantile(0.95)
        ]

