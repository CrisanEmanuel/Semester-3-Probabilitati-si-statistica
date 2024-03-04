from scipy.stats import binom
import numpy as np


def Y1Y2Y3():
    # Part (a): Generating Triplets and Estimating Probabilities

    N = 1000
    # Generate the vector w
    w = np.random.uniform(0, 5, 6)

    # Initialize variables for sum of products and favorable cases count
    sum_of_products = 0
    favorable_count = 0

    # Simulation
    for _ in range(N):
        Y1, Y2, Y3 = np.random.choice(w, 3, replace=True)
        product = Y1 * Y2 * Y3
        sum_of_products += product
        if Y1 + Y2 > Y3:
            favorable_count += 1

    # Calculate the average product and probability
    average_product = sum_of_products / N
    probability_Y1Y2_gt_Y3 = favorable_count / N

    # Part (b): Theoretical Probability Calculation

    # Parameters for the binomial distribution
    n = 6  # Number of trials (elements in w)
    p = 2 / 5  # Probability of success (element in [2, 4])

    # Probability of exactly 3 successes
    prob_exactly_3_in_interval = binom.pmf(3, n, p)

    return average_product, probability_Y1Y2_gt_Y3, prob_exactly_3_in_interval
