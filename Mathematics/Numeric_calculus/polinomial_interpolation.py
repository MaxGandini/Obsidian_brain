import numpy as np
import matplotlib.pyplot as plt
from typing import Callable

# Define the interpolator function
def interpolator(x: np.array, x_plot: np.array, function: Callable, derivative: Callable) -> np.array:
    n = len(x)  # Number of input points
    m = len(x_plot)  # Number of points to evaluate the polynomial
    
    # Step 1: Compute function and derivative values at x
    f_values = function(x)
    f_prime_values = derivative(x)
    
    # Step 2: Create the matrix M (Hermite Vandermonde-like system)
    M = np.zeros((2 * n, 2 * n))
    for i in range(n):
        # Populate rows for function values
        for j in range(2 * n):
            M[2 * i, j] = x[i] ** j  # f(x) rows
        # Populate rows for derivative values
        for j in range(1, 2 * n):
            M[2 * i + 1, j] = j * (x[i] ** (j - 1))  # f'(x) rows
    
    # Step 3: Construct the vector b
    b = np.zeros(2 * n)
    b[0::2] = f_values  # Assign f(x) values at even indices
    b[1::2] = f_prime_values  # Assign f'(x) values at odd indices
    
    # Step 4: Solve the linear system
    coeffs = np.linalg.solve(M, b)
    
    # Step 5: Evaluate the polynomial at points x_plot
    P_values = np.zeros(m)
    for i in range(m):
        x_val = x_plot[i]
        P_values[i] = sum(coeffs[j] * (x_val ** j) for j in range(2 * n))
    
    return P_values
# Example function and its derivative
def f(x):
    return np.sin(x)

def f_prime(x):
    return np.cos(x)

x = np.array([0, np.pi / 4, np.pi / 2,np.pi]) 

x_plot = np.linspace(0, np.pi*2, 100) 

polynomial_values = interpolator(x, x_plot, f, f_prime)

plt.plot(x_plot, polynomial_values, label="polinomio interpolado")
plt.plot(x, f(x), 'o', label="puntos")
plt.plot(x_plot, f(x_plot), label="Funcion real")
plt.legend()
plt.show()
