A perceptron is a [[Supervised-Learning]] algorithm. It works as a binary classifier, taking [[Tensors]] as inputs and deciding through the calculation of a number if the object represented by the input belongs to some specific class.

![[perceptron.png]]

The state of the previous layer can be written as $z$ :

$$ z = \sum_i x_i w_i + b$$

The [[Activation function]] can be written as the step function:

$$ \sigma(z) =\begin{cases}  1 \ if \ z\ge0 \\ 0 \ if \ z<0 \end{cases} $$

An interesting consequence of this, is that one can imagine the z function as a linear function and the sigma as an umbral function. We can construct logic gates with this concept.
AND gate:

| Out | $I_1$ | $I_2$ |
| --- | ----- | ----- |
| 0   | 0     | 0     |
| 0   | 0     | 1     |
| 0   | 1     | 0     |
| 1   | 1     | 1<br> |
By adjusting $b$ you can get an AND and an OR gate. But it was shown that and XOR gate can never be made with a unique line *z*. An example can be found in [[Perceptron.py]] .

In the context of neural nets, the perceptron is an artificial neuron([[Nodes]]) using the heaviside step function as the activation function. The [[Universal approximation theorem]] can be use to show that using a [[logistic function]] as an approximation will also work.