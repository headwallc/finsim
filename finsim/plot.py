import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def fmt_pct(x):
    e = int(x*100.0)
    return f'{e:,}%'


class Plot:
    def __init__(self):
        sns.set_theme()
        sns.set_style("ticks")

    def plot_returns(self, returns):
        fig, axs = plt.subplots(len(returns), figsize=(12, 12))

        bins = np.linspace(0, 60, 200)
        idx = 0
        for i in returns:
            r = returns[i].get_returns()
            ax = axs[idx]
            ax.set_title(i)
            ax.hist(r, density=1, bins=bins, label=i)
            # plot 5, 50, 95 quantiles
            qts = returns[i].get_quantiles_5_50_95()
            ax.axvline(x=qts[0], color='r', ls=':', lw=3)
            ax.axvline(x=qts[1], color='r', lw=3)
            ax.axvline(x=qts[2], color='r', ls=':', lw=3)
            # plot ticks
            ax.set_xticklabels(map(fmt_pct, ax.get_xticks())) #, rotation = 45)
            idx += 1

        plt.subplots_adjust(hspace=0.5)
        plt.grid()
        plt.show()
