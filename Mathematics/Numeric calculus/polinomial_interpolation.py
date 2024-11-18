import numpy as np 
from typing import Callable

def interpolator(x: np.array, x_plot: np.array, function: Callable, derivative: Callable) -> np.array:
    n = len(x)  
    m = len(x_plot)  
    
    f_values = function(x)
    f_prime_values = derivative(x)
    
    M = np.zeros((2 * n, 2 * n))  
    
    for i in range(n):
        # Fill in the rows corresponding to f(x_i)
        M[2 * i, 0] = 1
        for j in range(1, 2 * n):
            M[2 * i, j] = x[i] ** j
        
        M[2 * i + 1, 0] = 0
        for j in range(1, 2 * n):
            M[2 * i + 1, j] = j * x[i] ** (j - 1)
    
    b = np.zeros(2 * n)
    b[0::2] = f_values  
    b[1::2] = f_prime_values
    
    coeffs = np.linalg.inv(M).dot(b)
    
    P_values = np.zeros(m)
    
    for i in range(m):
        x_val = x_plot[i]
        P_values[i] = 0
        for j in range(n):
            term = coeffs[2 * j]  # f(x_j) coefficient
            for k in range(1, 2 * n):
                term *= x_val ** k
            P_values[i] += term
        
        for j in range(n):
            term = coeffs[2 * j + 1]  # f'(x_j) coefficient
            for k in range(1, 2 * n):
                term *= x_val ** k
            P_values[i] += term
    
    return P_values

import matplotlib.pyplot as plt

# Define the function f(x) and its derivative f'(x)
def f(x):
    return np.sin(x)

def f_prime(x):
    return np.cos(x)

x = np.array([0, np.pi / 4, np.pi / 2])  # Interpolation points
x_plot = np.linspace(0, np.pi / 2, 100)  # Points to evaluate the polynomial

# Call the interpolator function
polynomial_values = interpolator(x, x_plot, f, f_prime)

plt.plot(x_plot, polynomial_values, label="Interpolated Polynomial")
plt.plot(x, f(x), 'ro', label="Interpolation Points (f(x))")
plt.plot(x, f_prime(x), 'bo', label="Interpolation Points (f'(x))")
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x) and P(x)')
plt.title('Hermite Interpolation')
plt.show()
