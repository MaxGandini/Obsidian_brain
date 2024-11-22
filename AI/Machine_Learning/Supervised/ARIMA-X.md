It's a model that stands for Autoregressive integrated moving average. It's pretty self explanatory, but it's a model that generalizes autogressive moving average: ARMA(jaj).

It models non stationary series and periodic variation respectively. All these models are fitted to time series in order to better understand it an predict future values. 

Stationary series is a series which does not change it's expected value over time. There are also generalizations like SARIMA which take into account seasonal variations. 

![[ARIMA-8-1269249993.png]]

# Maths:

The ARIMA model is expressed as $ARIMA(p,d,q)$, combining the following components:

1. **AutoRegressive (AR)**: Relationship between current and past values.
2. **Integrated (I)**: Differencing to make the series stationary.
3. **Moving Average (MA)**: Dependency on past forecast errors.
### 1.Integration

To achieve stationarity, we apply differencing $d$-times to the series $y_t$ :

$$
y_t'=\Delta^d y_t=(1-B)^d y_t
$$

Where $B$ is the backshift operator defined as $B y_t=y_{t-1}$. It basically sends $y$ to the previous step. 

### 2. AutoRegressive 

The AR component of order $p$ is defined as:

$$
y_t'=\phi_1 y_{t-1}'+\phi_2 y_{t-2}'+\dots+\phi_p y_{t-p}'+\epsilon_t
$$

Equivalently:

$$
\Phi(B)y_t'=\epsilon_t
$$

Where $\Phi(B)=1-\phi_1 B-\phi_2 B^2-\dots-\phi_p B^p$.

### 3. Moving Average (MA) Component

The MA component of order $q$ is given by:

$$
y_t'=\epsilon_t+\theta_1 \epsilon_{t-1}+\theta_2 \epsilon_{t-2}+\dots+\theta_q \epsilon_{t-q}
$$

Equivalently:

$$
\Theta(B)\epsilon_t=y_t'
$$

Where $\Theta(B)=1+\theta_1 B+\theta_2 B^2+\dots+\theta_q B^q$.

### 4. Combining AR, I, and MA Components

The general ARIMA equation becomes:

$$
\Phi(B)(1-B)^d y_t=\Theta(B)\epsilon_t
$$

Where:
- $\Phi(B)$: AR polynomial.
- $(1-B)^d$: Differencing operator.
- $\Theta(B)$: MA polynomial.

### 5. Stationarity and Invertibility Conditions

- **Stationarity**: Roots of $\Phi(B)$ must lie outside the unit circle.
- **Invertibility**: Roots of $\Theta(B)$ must lie outside the unit circle.