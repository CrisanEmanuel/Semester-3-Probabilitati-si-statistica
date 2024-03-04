import numpy as np
from scipy.stats import hypergeom


def X1X2():
    # Part (a): Generating Pairs and Estimating Probabilities

    nr_sim = 1000
    # Generate the vector v
    v = np.random.uniform(0, 10, 5)

    # Initialize variables for sum of sums and favorable cases count
    total_sum = 0
    favorable_count = 0

    # Simulation
    for _ in range(nr_sim):
        X1, X2 = np.random.choice(v, 2, replace=False)
        sum_pair = X1 + X2
        total_sum += sum_pair
        if abs(X1 - X2) > 2:
            favorable_count += 1

    # Calculate the average sum and probability
    average_sum = total_sum / nr_sim
    probability_abs_diff_gt_2 = favorable_count / nr_sim

    # Part (b): Theoretical Probability Calculation

    # Parameters for the hypergeometric distribution
    N = 5  # Total number of objects (elements in v)
    K = 3  # Number of objects that are a success (in [5, 8])
    n = 2  # Number of draws
    k = 2  # Number of successes in n draws

    # Probability of exactly 2 successes
    prob_exactly_2_in_interval = hypergeom.pmf(k, N, K, n)

    return average_sum, probability_abs_diff_gt_2, prob_exactly_2_in_interval
