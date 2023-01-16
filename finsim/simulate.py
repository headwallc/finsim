import random


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


def calculate_terminal_gains(gains, finprod=lambda x: x, capital=1):
    current_capital = capital
    for g in gains:
        step = current_capital * (1 + finprod(g))
        current_capital = step
    return current_capital


