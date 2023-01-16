import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker


class Plot:
    def __init__(self):
        sns.set_theme()
        sns.set_style("ticks")

    def plot_returns(self, returns):
        data = {}
        for i in returns:
            data[i] = returns[i].get_returns()
        df = pd.DataFrame(data)

        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_title("Sim")
        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
        hist_data = ax.hist(df, density=1, bins=100)

        # ax.axvline(x=p5, color='r', ls=':', lw=3)
        # ax.axvline(x=p50, color='r', lw=3)
        # ax.axvline(x=p95, color='r', ls=':', lw=3)

        # l = ax.set_xticklabels(map(format_x, ax.get_xticks()))  # , rotation = 45)

        plt.grid()
