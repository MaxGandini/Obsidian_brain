---
id: PACF
aliases: []
tags: []
---

```python
statsmodels.tsa.stattools.acf(x, adjusted=False, nlags=None, qstat=False, fft=True, alpha=None, bartlett_confint=True, missing='none')
```

It measures the auto[[Correlation]] function of a time series at different lags. It helps identify patterns in the data.

For a stationary time series $X_t$, the autocorrelation function at lag $k$ is defined as:

$$\rho_k=\frac{\text{Cov}(X_t,X_{t+k})}{\sqrt{\text{Var}(X_t)\cdot\text{Var}(X_{t+k})}}$$

Where:
- $\text{Cov}(X_t,X_{t+k})$: The [[Covariance]] between $X_t$ and $X_{t+k}$.
- $\text{Var}(X_t)$: The variance of $X_t$.

If the time series is mean-centered (i.e., $\mu=0$), the formula simplifies to:

$$\rho_k=\frac{\sum_{t=1}^{N-k}(X_t\cdot X_{t+k})}{\sum_{t=1}^N X_t^2}$$

#### Correlation Function for Non-Stationary Time Series
For non-stationary time series, the autocorrelation function cannot be directly applied because the mean and variance may change over time. To handle non-stationarity:

1. **Detrending**: Remove trends from the time series using techniques like differencing or regression. Define a new time series $X'_t$ as:
   $$X'_t = X_t - \hat{\mu}_t$$
   Where $\hat{\mu}_t$ is an estimate of the trend or mean at time $t$.

2. **Autocorrelation of Residuals**: Compute the autocorrelation of the residual series $X'_t$:
   $$\rho_k=\frac{\text{Cov}(X'_t,X'_{t+k})}{\sqrt{\text{Var}(X'_t)\cdot\text{Var}(X'_{t+k})}}$$

3. **Cross-Correlation for Two Series**:
   For non-stationary time series $X_t$ and $Y_t$, use detrended series $X'_t$ and $Y'_t$ to compute the cross-correlation function:
   $$\rho_k^{XY}=\frac{\text{Cov}(X'_t,Y'_{t+k})}{\sqrt{\text{Var}(X'_t)\cdot\text{Var}(Y'_{t+k})}}$$

