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
    
    # Step 2: Create the matrix M (Vandermonde-like system)
    M = np.zeros((2 * n, 2 * n))  # Create an empty matrix of size (2n, 2n)
    
    for i in range(n):
        # Fill in the rows corresponding to f(x_i)
        M[2 * i, 0] = 1
        for j in range(1, 2 * n):
            M[2 * i, j] = x[i] ** j
        
        # Fill in the rows corresponding to f'(x_i)
        M[2 * i + 1, 0] = 0
        for j in range(1, 2 * n):
            M[2 * i + 1, j] = j * x[i] ** (j - 1)
    
    # Step 3: Construct the vector b
    b = np.zeros(2 * n)
    b[0::2] = f_values  # Assign f(x) values at even indices (0, 2, 4, ...)
    b[1::2] = f_prime_values  # Assign f'(x) values at odd indices (1, 3, 5, ...)
    
    # Step 4: Solve the system of linear equations to find the coefficients
    coeffs = np.linalg.inv(M).dot(b)
    
    # Step 5: Evaluate the polynomial at points x_plot
    P_values = np.zeros(m)
    
    for i in range(m):
        x_val = x_plot[i]
        P_values[i] = 0
        
        # Sum the polynomial terms for f(x) part
        for j in range(n):
            term = coeffs[2 * j]  # f(x_j) coefficient
            for k in range(1, 2 * n):
                term *= x_val ** k
            P_values[i] += term
        
        # Sum the polynomial terms for f'(x) part
        for j in range(n):
            term = coeffs[2 * j + 1]  # f'(x_j) coefficient
            for k in range(1, 2 * n):
                term *= x_val ** k
            P_values[i] += term
    
    return P_values

# Example function and its derivative
def f(x):
    return np.sin(x)

def f_prime(x):
    return np.cos(x)

# Example x values
x = np.array([0, np.pi / 4, np.pi / 2])  # 3 points
x_plot = np.linspace(0, np.pi / 2, 100)  # Points to evaluate the polynomial

# Call the interpolator function
polynomial_values = interpolator(x, x_plot, f, f_prime)

# Plot the results
plt.plot(x_plot, polynomial_values, label="Interpolated Polynomial")
plt.plot(x, f(x), 'o', label="Data Points")
plt.legend()
plt.show()
