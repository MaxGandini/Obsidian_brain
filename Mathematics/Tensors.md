Tensors are a fundamental concept in physics. They allow the description of a state that follows a certain equation, through various representations depending on a frame of reference, without changing the form of the equation that describes the physics.
(The intuition to follow is that the physical laws here, have to be the same as in mars or any other part of the universe)

![[tensor.png]]

IE: A vector is a rank 1 tensor. The rank is defined by amount of indices you need to describe the mathematical object. A matrix, can be a rank 2 tensor, as long as it follows the rules of tensor transformation.

As seen in the image, the tensor is not exactly the vector representation, it is a set of numbers that, given a set of basis vectors, can be used yo reconstruct some coordinate. (4,5,0)
Also, a vector can represent a unit of area perpendicular to it, bearing this in mind, one can interpret the second index of every triplet of vectors in the image as a force acting on a direction to the unit area of the faces of the cube.

Tensors are also, fundamental in [[AI]] , as they are the input and output for [[Neural Networks]] and [[Machine Learning]] models.
This is so, because [[Neural Networks]] work with [[Nodes]] and coefficients that represent activation. Each node is a state of the net, and the set of coefficients representing the activation is a tensor.