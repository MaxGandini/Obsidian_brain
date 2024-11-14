from typing import List, Callable
import numpy as np

type vector = np.array

# We define a perceptron class, with it, we can make logic gates like nans and ors. These can be thought of a bias-adjusted perceptron.

class perceptron:
    '''
    Many instances can define a perceptron in a network.
    It is initialized by a bias, a weight and an activation function.
    It is an abstraction of the element that constitutes a neuron in the network.
    '''
    def __init__(self,bias:float,weight,activation_function:Callable):
        self.weight = [_ for _ in weight]
        self.bias = bias
        self.activation_function = activation_function

    def compute(self,input:vector):
        weighted_sum = sum([input[i]*self.weight[i] for i in range(len(self.weight))]) + self.bias
        computation = self.activation_function(weighted_sum)

        return computation

def activation_heaviside(sum:float) -> float:
    '''
    Heaviside/step function
    '''
    activation = 1 if sum >= 0 else 0
    return activation

vector_ = np.array([1,0])
weights = [ 0.5 for _ in vector_]
bias = 0

perceptron0 = perceptron(bias,weights,activation_heaviside)

print(perceptron0.compute(vector_))

or_gate = perceptron(-0.5, weights, activation_heaviside)

print(or_gate.compute(vector_))
state_0 = np.array([1,0])

print(or_gate.compute(state_0))

## We take on the challenge of making an XOR gate. It is intuitive that we shall need two input functions. 
## Also, an XOR gate can be thought of as an and gate and an or gate 


