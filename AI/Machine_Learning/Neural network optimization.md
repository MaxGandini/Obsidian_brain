The optimization of a neural network is a gradient descent problem.

We define the cost function as:

$$C({W}) = \sum_{training} (f(X,W)-y_{data})^2$$
Which is the squared error of the system function and all the cases of the training data. In principle, the problem is no different than a typical gradient descent, where you iterate with the derivative of the error function and get the best case of your iteration:

$$ \vec{W'}  = \vec{W} - \eta  \vec{\nabla } C$$

![[gradient.png]]


Gradient Descent is an optimization algorithm used to minimize the cost function in neural networks by iteratively adjusting the weights to reduce error.

For a neural network with a cost function $C$, Gradient Descent updates the weights $w$ and biases $b$ to minimize $C$.

The update rule for weights $w$ and biases $b$ is:

$$w \rightarrow w - \alpha \frac{\partial C}{\partial w}$$

$$b \rightarrow b - \alpha \frac{\partial C}{\partial b}$$

where:
- $\alpha$ is the **learning rate** (a small positive constant),
- $\frac{\partial C}{\partial w}$ is the **partial derivative** of the cost function with respect to weight $w$,
- $\frac{\partial C}{\partial b}$ is the **partial derivative** of the cost function with respect to bias $b$.
F
![[neural_gradient.png]]

### Cost Function and Gradient

The cost function $C$ (often Mean Squared Error or Cross-Entropy) quantifies the difference between the predicted and actual outputs. Minimizing $C$ helps the network make accurate predictions.

The **gradient** $\nabla C$ of $C$ with respect to weights $w$ and biases $b$ is:

$$\nabla C = \left( \frac{\partial C}{\partial w_1}, \frac{\partial C}{\partial w_2}, \dots, \frac{\partial C}{\partial w_n}, \frac{\partial C}{\partial b_1}, \frac{\partial C}{\partial b_2}, \dots, \frac{\partial C}{\partial b_m} \right)$$

where $n$ and $m$ are the total number of weights and biases, respectively. The gradient $\nabla C$ points in the direction of the steepest increase in $C$, so subtracting it (scaled by $\alpha$) moves toward a minimum.

### Iterative Update Process

For each training example, the Gradient Descent algorithm computes the gradient $\nabla C$ and updates the weights and biases as follows:

1. Compute the prediction and calculate the cost $C$.
2. Compute the **gradients** $\frac{\partial C}{\partial w}$ and $\frac{\partial C}{\partial b}$.
3. Update each weight and bias using:

   $$w \rightarrow w - \alpha \frac{\partial C}{\partial w}$$
   
   $$b \rightarrow b - \alpha \frac{\partial C}{\partial b}$$

4. Repeat this process for each batch or epoch until $C$ reaches an acceptable minimum.

### Mini-Batch Gradient Descent

In practice, **Mini-Batch Gradient Descent** is often used. Instead of computing $\nabla C$ for each individual example, it averages the gradient over a small batch of examples. This stabilizes updates and reduces computation time.

If $B$ is a batch of examples, the gradient for the batch is:

$$\nabla C = \frac{1}{|B|} \sum_{i \in B} \nabla C_i$$

### Summary

- **Gradient Descent** adjusts weights and biases in the opposite direction of the gradient to minimize $C$.
- The **learning rate** $\alpha$ controls the step size.
- **Mini-Batch Gradient Descent** further optimizes efficiency and stability by averaging gradients over a batch.

This iterative update process is foundational for training neural networks effectively.
