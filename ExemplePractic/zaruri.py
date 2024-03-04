import numpy as np


def zaruri(N=1000):
    # Probability of rolling a double
    p_double = 1 / 6

    # Simulate N trials
    trials = np.random.geometric(p_double, N) - 1  # Subtract 1 for unsuccessful throws

    # Calculate probabilities for events A, B, C
    prob_A = np.mean(trials > 3)
    prob_B = np.mean((trials >= 5) & (trials <= 10))
    prob_C = np.mean(trials[trials > 3] >= 5)

    return prob_A, prob_B, prob_C
