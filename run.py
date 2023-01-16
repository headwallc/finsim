from finsim.arena import Arena
from finsim.data import SP500, NASDAQ
from finsim.investment import Investment
from finsim.plot import Plot
from finsim.product import FP_IDEM, FP_VALUE_FLOOR_0_CAP_10, FP_UNCAPPED_FLOOR_0_SPREAD_8


def main():
    arena = Arena()
    arena.add_investment(Investment(SP500, FP_IDEM))
    arena.add_investment(Investment(SP500, FP_VALUE_FLOOR_0_CAP_10))
    arena.add_investment(Investment(SP500, FP_UNCAPPED_FLOOR_0_SPREAD_8))
    arena.add_investment(Investment(NASDAQ, FP_IDEM))
    arena.add_investment(Investment(NASDAQ, FP_VALUE_FLOOR_0_CAP_10))
    arena.add_investment(Investment(NASDAQ, FP_UNCAPPED_FLOOR_0_SPREAD_8))

    arena.simulate(N=10000)
    arena.print_results()

    plot = Plot()
    plot.plot_returns(arena.get_returns())


if __name__ == '__main__':
    main()
