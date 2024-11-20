import numpy as np
from typing import Callable

def interpolator(x: np.array, x_plot: np.array, function: Callable, derivative: Callable) -> np.array:
    '''
    Los inputs y outputs de la funcion estan definidos usando "type hinting" de python. 
    El metodo en si usa matriz de vandermonde ya que es el metodo mas facil de calcular conceptualmente
    (usando el modulo linalg de numpy)
    '''
    n = len(x)   
    m = len(x_plot) #el que vamos a usar para plotear
    
    f_values = function(x)
    f_prime_values = derivative(x)
    
    M = np.zeros((2 * n, 2 * n)) # matriz del pol

    for i in range(n):
        for j in range(2 * n):
            M[2 * i, j] = x[i] ** j  
        for j in range(1, 2 * n):
            M[2 * i + 1, j] = j * (x[i] ** (j - 1))  
    
    b = np.zeros(2 * n) # armo los coeficientes
    b[0::2] = f_values  
    b[1::2] = f_prime_values  
    
    coeffs = np.linalg.solve(M, b) # Resuelvo el sistema M * coef
    
    P_values = np.zeros(m)

    for i in range(m): #calculo los valores del polinomio en cada punto para la variable continua
        x_val = x_plot[i]
        P_values[i] = sum(coeffs[j] * (x_val ** j) for j in range(2 * n))
    
    return P_values

import matplotlib.pyplot as plt
def f(x):
    return 1/(1+25*(x**2))

def f_prime(x):
    return -50**x/((1+25*(x**2))**2)

x = np.array([0, np.pi / 4, np.pi / 2,np.pi]) 

x_plot = np.linspace(0, 3.5, 100) 

polynomial_values = interpolator(x, x_plot, f, f_prime)

plt.plot(x_plot, polynomial_values, label="polinomio interpolado")
plt.plot(x, f(x), 'o', label="puntos")
plt.plot(x_plot, f(x_plot), label="Funcion real")

plt.legend()
plt.show()
