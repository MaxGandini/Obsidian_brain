Qualitative graph of how the logistic function looks:

![[_Attachments/Diagram.svg]]

$$
P(Y=1 | X) = \sigma(z) = \frac{1}{1 + e^{ k(z - z_0)}}
$$

where

$$
z = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \ldots + \beta_n X_n
$$

and

- $P(Y=1 | X)$ is the probability that the output $Y$ is 1 given the input features $X$.
- $\sigma(z)$ is the logistic function.
- $\beta_0$ is the intercept.
- $\beta_1, \beta_2, \ldots, \beta_n$ are the coefficients associated with each feature $X_1, X_2, \ldots, X_n$.

An important feature to recognize here, is that as k becomes bigger, the logistic function tends to a Heaviside theta function. Also, $z_0$ marks an offset, but most of the times, it is set to 0.

