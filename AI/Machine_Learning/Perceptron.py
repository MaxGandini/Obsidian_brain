from typing import List, Callable
import numpy as np

type vector = np.array

class perceptron:

    def __init__(self,bias:float,weight,activation_function:Callable):
        self.weight = [_ for _ in weight]
        self.bias = bias
        self.activation_function = activation_function

    def compute(self,input:vector):
        weighted_sum = sum([input[i]*self.weight[i] for i in range(len(self.weight))]) + self.bias
        computation = self.activation_function(weighted_sum)

        return computation

def activation_heaviside(sum:float) -> float:
    activation = 1 if sum >= 0 else 0
    return activation

vector_ = np.array([1,0])
weights = [ 0.5 for _ in vector_]
bias = 0

perceptron0 = perceptron(bias,weights,activation_heaviside)

print(perceptron0.compute(vector_))

or_gate = perceptron(-0.5, weights, activation_heaviside)

print(or_gate.compute(vector_))
state_0 = np.array([0,0])

print(or_gate.compute(state_0))

# def perceptron_a(input:vector, bias:float) -> float:
#     w = [0.5 for _ in input]
#     weighted_sum = sum(w[i] * input[i] for i in range(len(input))) + bias
#
#     function = activation_heaviside(weighted_sum)
#
#     return function
#
#
# input_vector = [1.0,0.0]  # Replace with your input values
# or_output = perceptron_a(input_vector, -0.5)
# and_output = perceptron_a(input_vector, -1.5)
#
# print(f"Output of the perceptron: {or_output}")
# print(f"Output of the perceptron: {and_output}")
#
#
