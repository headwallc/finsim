import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def fmt_pct(x):
    e = int((x - 1) * 100.0)
    return f'{e:,}%'


class Plot:
    def __init__(self):
        sns.set_theme()
        sns.set_style("ticks")

    def plot_returns(self, returns):
        fig, axs = plt.subplots(len(returns), figsize=(12, 16))
        fig.suptitle(f'Simulated capital gain after 20 years')

        bins = np.linspace(0, 60, 300, endpoint=False)
        idx = 0
        for i in returns:
            r = returns[i].get_returns()
            ax = axs[idx]
            ax.set_title(i)
            ax.set_xlim(0, 15)
            ax.hist(r, density=1, bins=bins, label=i)
            # plot 5, 50, 95 quantile lines
            qts = returns[i].get_quantiles_5_50_95()
            legend_elements = [
                ax.axvline(x=qts[0], color='r', ls=':', lw=2),
                ax.axvline(x=qts[1], color='r', lw=2),
                ax.axvline(x=qts[2], color='gray', ls=':', lw=2)
            ]
            # plot legend
            qts_rounded = [round(x, 2) for x in qts]
            ax.legend(legend_elements, [
                f"95% : {fmt_pct(qts_rounded[0])}",
                f"50% : {fmt_pct(qts_rounded[1])}",
                f"5% : {fmt_pct(qts_rounded[2])}"
            ], loc="upper right")
            # plot ticks
            ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
            ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
            ax.set_xticklabels(map(fmt_pct, ax.get_xticks()))  # , rotation = 45)
            idx += 1

        plt.subplots_adjust(hspace=0.6)
        plt.grid()
        plt.show()
