import numpy as np
from scipy.stats import expon


def server1(N=1000):
    # Define the server selection probabilities and exponential distribution means
    servers = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    total_time = 0
    count_at_least_3s = 0

    # Simulation
    for _ in range(N):
        selected_server = np.random.choice(servers)
        processing_time = expon.rvs(scale=selected_server)  # scale parameter is the mean for exponential distribution
        total_time += processing_time

        if processing_time >= 3:
            count_at_least_3s += 1

    # Calculate average processing time and probability of processing time being at least 3 seconds
    average_time = total_time / N
    prob_at_least_3s = count_at_least_3s / N

    return average_time, prob_at_least_3s
