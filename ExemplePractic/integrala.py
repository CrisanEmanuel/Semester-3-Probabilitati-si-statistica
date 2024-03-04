import numpy as np
from scipy.integrate import quad
# Define the function f(x)
def f(x):
    return 1 / (x + 1) ** 2
def integrala():
    # Part (a): Approximate the integral value
    # Generate 1000 points in the square [0,1]x[0,1]
    simulariX = np.random.uniform(0, 1, 1000)

    # Calculate the values of f(x) for the simulated points
    simulariFX = f(simulariX)

    # The Monte Carlo estimate for the integral is the mean of the function values
    integral_estimate = np.mean(simulariFX)

    # Part (b): Theoretical probability that a point lies above the graph of f, given its x is in [0,0.5]
    # Calculate the area under the curve from 0 to 0.5 using numerical integration
    integral_area, _ = quad(f, 0, 0.5)

    # The probability is 1 minus the ratio of the integral area to the rectangle area (0.5)
    probability_above_graph = 1 - (integral_area / 0.5)

    return integral_estimate, probability_above_graph
