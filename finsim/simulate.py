import random


def simulate_gains(pool, k=20):
    return [random.choice(pool) for x in [] * k]


def simulate_gain_matrix(pool, k=20, N=1000):
    """
    Bootstrap N random gain vectors of length k from provided gain pool.
    :param pool: list of gains
    :param k: years simulated
    :param N: number of simulations
    :return: k x N matrix of gains
    """
    matrix = [[]] * N
    for i in range(N):
        matrix[i] = simulate_gains(pool, k)
    return matrix


def simulate_terminal_gains(pool, k=20, N=1000, capital=1):
    res = [] * N
    for i in range(N):
        current_capital = capital
        for y in range(k):
            current_capital = current_capital * (1 + random.choice(pool))
        res[i] = current_capital
    return res


def apply_captial(capital, gains):
    res = [capital]
    for g in gains:
        res.append(res[-1] * (1 + g))
    return res


print(apply_captial(270000, nasdaq))
