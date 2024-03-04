from scipy.stats import expon, uniform


def server2(N=1000):
    total_time = 0
    processed_in_4s = 0
    processed_in_3s_probability = expon.cdf(3, scale=4)  # Theoretical probability for processing within 3 seconds

    # Simulation
    for _ in range(N):
        t1 = expon.rvs(scale=4)  # Exponential distribution with mean 4 seconds
        t2 = uniform.rvs(1, 2)  # Uniform distribution between 1 and 3 seconds
        time_processed = t1 if t1 <= 4 else (4 + t2)
        total_time += time_processed

        if time_processed <= 4:
            processed_in_4s += 1

    # Calculate average processing time and probability of processing within 4 seconds
    average_time = total_time / N
    prob_processed_in_4s = processed_in_4s / N

    return processed_in_3s_probability, average_time, prob_processed_in_4s
