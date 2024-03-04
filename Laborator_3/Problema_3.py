from random import randrange

from matplotlib.pyplot import hist, bar, legend, grid, show
from scipy.stats import binom


def histograma_trei(alegeriX):
    data = binom.rvs(5, 0.6, 10000)
    bin_edges = [k + 0.5 for k in range(-1, 6)]
    hist(data, bin_edges, density=True, rwidth=0.9, color='green', edgecolor='black',
         alpha=0.5, label='frecvente relative')
    distribution = dict([(i, binom.pmf(i, 5, 0.6)) for i in range(1, 6)])
    bar(distribution.keys(), distribution.values(), width=0.85, color='red', edgecolor='black',
        alpha=0.6, label='probabilitati')
    legend(loc='lower left')
    grid()
    show()
    print("\n")


def simulare25(alegeriX):
    nr_caz_fav = 0
    nr_caz_posibile = len(alegeriX)
    for i in alegeriX:
        if 2 < i <= 5:
            nr_caz_fav += 1
    return nr_caz_fav / nr_caz_posibile
