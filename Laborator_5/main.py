import matplotlib.pyplot as plt
from matplotlib.pyplot import show, hist, grid, legend, xticks, plot
from scipy.stats import expon
import numpy as np

'''
Problema 1
'''


def generate_discrete_random_variable(values, probabilities, n):
    cumulative_probabilities = np.cumsum(probabilities)
    random_numbers = np.random.uniform(0, 1, n)

    result = np.zeros(n, dtype=int)

    for i in range(n):
        for j in range(len(cumulative_probabilities)):
            if cumulative_probabilities[j - 1] < random_numbers[i] <= cumulative_probabilities[j]:
                result[i] = values[j]
                break

    return result


def problema_1():
    blood_types = np.array([0, 1, 2, 3])  # 0 - O, 1 - A, 2 - B, 3 - AB
    probabilities = np.array([0.46, 0.40, 0.10, 0.04])

    N = 1000

    simulated_blood_types = generate_discrete_random_variable(blood_types, probabilities, N)

    unique, counts = np.unique(simulated_blood_types, return_counts=True)
    observed_frequencies = counts / N

    for blood_type, frequency in zip(unique, observed_frequencies):
        print(f"Grupa sanguină {blood_type}: Frecvență relativă - {frequency:.2f}")

    plt.bar(unique, observed_frequencies, label="Observate", alpha=0.7)
    plt.bar(blood_types, probabilities, label="Teoretice", alpha=0.7)
    plt.xlabel("Grupa sanguină")
    plt.ylabel("Frecvență relativă")
    plt.legend()
    plt.show()


'''problema_1()'''

'''
Problema 2 - 0.6592
'''


def problema_2_aplicatie():
    alpha = 1

    N = 1000

    print_times = expon.rvs(scale=1 / alpha, size=N)

    plt.hist(print_times, bins=20, density=True, alpha=0.7, color='blue', edgecolor='black')

    x = np.linspace(0, max(print_times), 1000)
    plt.plot(x, expon.pdf(x, scale=1 / alpha), 'r-', label='Exponential')

    plt.xlabel('Print Time (seconds)')
    plt.ylabel('Probability Density')
    plt.legend()

    plt.show()


def problema_2_a():
    alpha = 1/12

    N = 1000

    print_times = expon.rvs(scale=1 / alpha, size=N)

    hist(print_times, bins=12, density=True, range=(0, 60), alpha=0.7, color='blue', edgecolor='black')

    x = range(60)
    plot(x, expon.pdf(x,loc=0, scale=1 / alpha), 'r-', label='Exponential')

    xticks(range(0, 60, 5))
    grid()
    legend()

    show()


def problema_2_b():
    min_duration = 5
    alpha = 1 / 12
    N = 1000
    print_times = -1 / alpha * np.log(1 - np.random.uniform(size=N))

    count_E = np.sum(print_times >= min_duration)
    P_E_estimata = count_E / N

    print(f'Probabilitatea estimata pentru P(E): {P_E_estimata:.4f}')

    P_E_theoretical = 1 - expon.cdf(min_duration, scale=1 / alpha)
    print(f'Probabilitatea teoretică pentru P(E): {P_E_theoretical:.4f}')


problema_1()
problema_2_aplicatie()
problema_2_a()
problema_2_b()
