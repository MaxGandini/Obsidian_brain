It's a function that takes a set of numbers [[Tensors]] as an input, and calculates a real number, which represents the weight, or activation of the node/neuron. 
Generally, it's a non-linear function. There's a reason for this, which is that the [[Universal Approximation Theorem]] proves that a two-layer neural network can be proven to be a universal function approximator as long as it is non-linear.

For the case of the [[Perceptron]], one can use a heaviside theta function or a [[logistic function]]. 