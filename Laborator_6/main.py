import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from scipy.stats import norm, expon
from scipy.stats import uniform
from numpy import exp, mean
from scipy.integrate import quad


def ex1A():
    m = 165
    sigma = 10
    n = [1000, 2000, 5000]

    for num_samples in n:
        heights = np.random.normal(m, sigma, num_samples)
        plt.hist(heights, bins=16, range=(130, 210), density=True, alpha=0.5, label=f'n = {num_samples}')
        x = np.linspace(130, 210, 1000)
        pdf = norm.pdf(x, m, sigma)
        plt.plot(x, pdf, label='Functie de densitate', linewidth=2)

    plt.title('Histograma si Functie de Densitate a Inaltimilor')
    plt.xlabel('Inaltime (cm)')
    plt.ylabel('Frecventa relativa / Densitate')
    plt.legend()
    plt.grid(True)
    plt.show()


def ex1BC():
    m = 165
    sigma = 10
    n_simulations = [1000, 2000, 5000]

    for num_samples in n_simulations:
        heights = np.random.normal(m, sigma, num_samples)
        mean_simulated = np.mean(heights)
        std_dev_simulated = np.std(heights)
        proportion_simulated = np.sum((heights >= 160) & (heights <= 170)) / num_samples
        mean_exact = m
        std_dev_exact = sigma
        proportion_exact = norm.cdf(170, m, sigma) - norm.cdf(160, m, sigma)
        print(f"Simulare pentru n = {num_samples}:")
        print(f"Valoare medie simulata: {mean_simulated:.2f} vs Valoare medie exacta: {mean_exact}")
        print(f"Deviatie standard simulata: {std_dev_simulated:.2f} vs Deviatie standard exacta: {std_dev_exact}")
        print(f"Proportia in intervalul [160, 170] simulata: {proportion_simulated:.4f} vs Proportia exacta: {proportion_exact:.4f}\n")


def ex2():
    def generate_T1_samples(n_samples):
        return np.random.exponential(scale=5, size=n_samples)

    def generate_T2_samples(n_samples):
        return np.random.uniform(low=4, high=6, size=n_samples)

    p_I1 = 0.4
    p_I2 = 0.6

    num_samples = 10000
    samples_T1 = generate_T1_samples(int(num_samples * p_I1))
    samples_T2 = generate_T2_samples(int(num_samples * p_I2))

    mean_T1 = np.mean(samples_T1)
    std_T1 = np.std(samples_T1)
    mean_T2 = np.mean(samples_T2)
    std_T2 = np.std(samples_T2)

    mean_time = p_I1 * mean_T1 + p_I2 * mean_T2
    std_time = np.sqrt(p_I1 * std_T1 * 2 + p_I2 * std_T2 * 2)

    print(f"Valoarea medie a timpului de printare: {mean_time:.2f} secunde")
    print(f"Deviatia standard a timpului de printare: {std_time:.2f} secunde")
    prob_I1_less_than_5 = expon.cdf(5, loc=0, scale=5)
    prob_I2_less_than_5 = 1 / 2

    prob_empirical = 0.4 * prob_I1_less_than_5 + 0.6 * prob_I2_less_than_5
    print(f"Probabilitatea teoretica  ca timpul de printare este mai mic de 5 secunde: {prob_empirical:.4f}")

    prob_empirical_sim = (np.sum(samples_T1 < 5) + np.sum(samples_T2 < 5)) / num_samples
    print(f"Probabilitatea estimata ca timpul de printare este mai mic de 5 secunde (prin simulare): {prob_empirical_sim:.4f}")


def ex3():
    def f(x):
        return exp(-x ** 2)

    a, b = -1, 3
    num_samples = 5000

    samples = uniform.rvs(loc=a, scale=b - a, size=num_samples)
    values = f(samples)

    monte_carlo_estimate = (b - a) * mean(values)
    integral, _ = quad(f, a, b)

    print(f'Estimarea Monte Carlo a integralei: {monte_carlo_estimate:.4f}')
    print(f'Valoarea exacta a integralei: {integral:.4f}')


if __name__ == '__main__':
    ex1A()
    ex1BC()
    ex2()
    ex3()