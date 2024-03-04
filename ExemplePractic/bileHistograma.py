import numpy as np
from scipy.stats import hypergeom
import matplotlib.pyplot as plt


def bileHistograma():
    # Set up the urn
    nr_sim = 5000
    urna = ['n'] * 8 + ['a'] * 4  # 'n' for black, 'a' for white

    cntA = 0  # Count for exactly 2 white balls
    cntB = 0  # Count for all black balls
    bile_albe = np.zeros(nr_sim)  # Track the number of white balls drawn

    # Simulation
    for i in range(nr_sim):
        bile_extrase = np.random.choice(urna, 4, replace=False)
        albe = np.sum(bile_extrase == 'a')

        if albe == 2:
            cntA += 1
        if albe == 0:
            cntB += 1

        bile_albe[i] = albe

    # Estimated probabilities
    probA_estimated = cntA / nr_sim
    probB_estimated = cntB / nr_sim

    # Theoretical probabilities using hypergeometric distribution
    probA_theoretical = hypergeom.pmf(2, 12, 4, 4)
    probB_theoretical = hypergeom.pmf(0, 12, 8, 4)

    # Histogram for the white balls drawn
    plt.figure()
    plt.hist(bile_albe, bins=20, weights=np.ones(nr_sim) / nr_sim)
    plt.title('Histograma frecventelor relative pentru bile albe extrase')
    plt.xlabel('Numărul de bile albe extrase')
    plt.ylabel('Frecvența relativă')
    plt.show()

    # Mean of white balls drawn
    mean_white_balls = np.mean(bile_albe)

    return probA_estimated, probB_estimated, probA_theoretical, probB_theoretical, mean_white_balls
