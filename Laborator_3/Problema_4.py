import random
from itertools import product

from matplotlib.pyplot import grid, show, bar, legend


def problema4():
    distribution_teoretica = dict([i, 0] for i in range(3, 19))
    for z in product(range(1, 7), repeat=3):
        distribution_teoretica[sum(z)] += 1 / 216

    nr_simulari = 10000
    distribution_simulare = dict([(i, 0) for i in range(3, 19)])
    for i in range(nr_simulari):
        nr1 = random.randrange(1, 7)
        nr2 = random.randrange(1, 7)
        nr3 = random.randrange(1, 7)
        suma = nr1 + nr2 + nr3
        distribution_simulare[suma] += 1 / nr_simulari

    bar(distribution_teoretica.keys(), distribution_teoretica.values(), width=0.85, color='red', edgecolor='black',
        alpha=0.6, label='prob teoretica')
    bar(distribution_simulare.keys(), distribution_simulare.values(), width=0.85, color='blue', edgecolor='black',
        alpha=0.6, label='prob simulare')
    legend(loc='best')
    grid()
    show()
