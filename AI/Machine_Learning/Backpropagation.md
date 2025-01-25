Backpropagation is an often misunderstood algorithm, it generally is mentioned in the context of neural networks within machine learning. It's an algorithm that can be used in the context of any optimization problem that involves a function with a set of undefined parameters and an array of points to which this function should adhere to.

A great explanation can be seen in the [[Artem Kisanov]] video about this algorithm: (https://youtu.be/SmZmBKc7Lrs)

But in synthesis, if one can reduce a problem to a [[Gradient descent]] problem, backpropagation can be applied. After initializing the model with some weights, one can iterate over and over while changing these through some criterion and calculate the difference of the loss function. 

The update rule for weights $w$ and biases $b$ is (See [[Gradient descent]]):

$$w \rightarrow w - \alpha \frac{\partial C}{\partial w}$$

$$b \rightarrow b - \alpha \frac{\partial C}{\partial b}$$

Through this difference, one then calculates the gradient, which gives the direction of maximum growth for the loss function (We are trying to minimize it).