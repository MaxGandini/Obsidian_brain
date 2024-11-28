It's the Bayesian Information Criterion.
It's similar to [[AIC]] but it penalizes model complexity in a more conservative way:

$$BIC= -2ln(L) + kln(n)$$
Where $L$ is the [[Likelihood]] of data, $k$ is the parameter number and $n$ is the number of data points in the dataset.

It's more robust to overfitting than AIC, and when $n$ is large it tends to prioritize simpler models.
