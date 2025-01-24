Akaike Information Criterion.
It measures the relative quality of statistical models for a given dataset, it takes into account:

- Fit
- Complexity

Formula: 

$$AIC = -2ln(L) + 2k$$
Where $L$ is the maximum likelihood of the model, and $k$ is the number of parameters. In the case of the ARIMA model, we have that k: 

$$k = p + q + k$$

It is applied for selecting the optimal lag length in models like [[ARIMA-X]]. How to interpret:

Smaller AIC values indicate a better trade-off between the goodness of the fit and the complexity
