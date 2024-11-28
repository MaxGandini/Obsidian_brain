It's a model that stands for Autoregressive integrated moving average. It's pretty self explanatory, but it's a model that generalizes autogressive moving average: [[ARMA]] (jaj).

It models non stationary series and periodic variation respectively. All these models are fitted to time series in order to better understand it an predict future values. 

Stationary series is a series which does not change it's expected value over time. There are also generalizations like SARIMA which take into account seasonal variations. 

The model has 3 hyperparameters to tune and their significance can be understood  mnemotechnically:

- ${\displaystyle {\text{ARIMA}}(1,0,0)}$⁠ is $AR(1)$ this autoregressive component means that the evolving variable of interest is regressed on it's previous values.
- $⁠{\displaystyle {\text{ARIMA}}(0,0,1)}⁠$ is $MA(1).$ This part indicates that the Moving average is formed by a regression error that is a linear combination of error terms whose values ocurred contemporaneously in the past.
- $⁠{\displaystyle {\text{ARIMA}}(0,1,0)}⁠$ is $I(1).$ The integrated part means that the values have been replaced with the difference between each value and the previous one.

The notation is: 
$$ARIMA(p,d,q)$$
- $p$ refers to the number of time lags.
- d is the degree of differencing. which is the amount of times the data had past values substracted.
- q is the order of the moving average model.

Toy example:
[[arima_toy.py]] 
Better example using statsmodels WIP: 
[[arima_function.py]]

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