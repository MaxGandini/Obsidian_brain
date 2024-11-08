A neural network is a [[Machine Learning]] model that is inspired in the concept of neurons in the brain.
Neurons are electrical units in the brain which have a certain activation given by pulses (In the brain, the response is highly non linear and it has memristive properties).

In an [[AI]] context, we have a representation of neurons as [[Nodes]]. These nodes have real coefficients associated with them which represent the node activation (AKA Weights).
Each node has a set of *edges* which represent the synapses between the neurons. 

![[neural.png]]

Neural networks typically come in the form of a set of layered neurons. 
Each set can be represented with [[Tensors]], which can be transformed when fed to a layer through a non-linear function called [[Activation function]] 
