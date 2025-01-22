---
id: ARIMA-differencing
aliases: []
tags: []
---

Excelent explanation from the wiki for differencing:

"A stationary time series's properties do not change. Specifically, for a wide-sense stationary time series, the mean and the variance/autocovariance are constant over time. Differencing in statistics is a transformation applied to a non-stationary time-series in order to make it stationary in the mean sense (that is, to remove the non-constant trend), but it does not affect the non-stationarity of the variance or autocovariance. Likewise, seasonal differencing is applied to a seasonal time-series to remove the seasonal component.

From the perspective of signal processing, especially the Fourier spectral analysis theory, the trend is a low-frequency part in the spectrum of a series, while the season is a periodic-frequency part. Therefore, differencing is a high-pass (that is, low-stop) filter and the seasonal-differencing is a comb filter to suppress respectively the low-frequency trend and the periodic-frequency season in the spectrum domain (rather than directly in the time domain)."

Mathematically:

$$ y_t^* = y_t ' - y_{t-1}' = (y_t - y_{t-1}) - (y_{t-1} - t_{t-2}) = y_t - 2y_{t-1} + y_{t-2}$$

It follows that $y_t'$ is the difference between the value at time $t$ and $t-1$, and that the formula can be expanded recursively.
Also, $y_t^*$ is the second order differencing of the data, and so on.
