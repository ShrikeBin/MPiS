import numpy as np
import matplotlib.pyplot as plt

# Mersenne Twister
rng = np.random.default_rng()  

def f(x):
    return np.sin(x)  

def g(x):
    return 4*x*((1-x)**3)

def h(x):
    return x ** (1/3)


def monte_carlo_integration(func, lower, upper, n, rng):
    x_random = rng.uniform(lower, upper, n) 
    func_values = func(x_random)
    estimate = (upper - lower) * np.mean(func_values)
    return estimate

def run_for_n(n_values,func, lower, upper, n, rng):
    results = []
    for n in n_values:
        estimate = monte_carlo_integration(func, lower, upper, n, rng)
        results.append(estimate)
    return results
    
n_values = [10, 100, 1000, 10000, 50000]
average_result = np.mean(results)

plt.figure(figsize=(10, 6))
plt.plot(n_values, results, marker='o', label="Monte Carlo Estimate")
plt.axhline(y=average_result, color='r', linestyle='--', label="Average Estimate")
plt.xlabel("Amount of points (n)")
plt.ylabel("Integral")
plt.xscale("log")
plt.legend()
plt.title("Monte Carlo Integral")
plt.savefig("plot.png")

