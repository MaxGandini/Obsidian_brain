Arma is the non-integrated version for [[ARIMA-X]] . It is an auto-regressive model with a shifting mean. Given a time series data array called : $X_t$

It can be modeled as : 

$$X_t = c + \sum_i^p \phi_i X_{t-i} + \epsilon_t $$

Where $\phi_i$ are the model parameters, $\epsilon_t$ is the error term and $c$ is a constant. This is based on a model for a circuit that is called IIR circuit(Infinite response circuit). It is called so because it has a feedback loop where the output always depends on its previous inputs through a feedback loop.

Toy mathematical example: 

####  AR(1) model: 


$$X_t = x + \phi X_{t-1} + \epsilon_t $$ 
Notice that the one represents the order of the model, in this case the $\epsilon$ represents white noise with 0 mean and variance $\delta^2$ .The subindex in $\phi$ was ommited. The process is stationary in it's [[Covariance]] if $\phi < 1$ .

Assuming a stationary covariance, we have: 
$$E(X_t)=E(c) + \phi E(X_{t-1}) + E(\epsilon_t) \rightarrow \mu = c + \phi \mu +0 $$
for the expectation value. 
Then: 
$$\mu = \frac{c}{1-\phi}$$
and we can calculate the variance: 

$$var(X_t) = E(X_t^2) - \mu^2 = \frac{\delta^2}{1-\phi^2}$$ And now the physics intuition! :

$$ \Phi(w) = \frac{1}{\sqrt{2\pi}} (\frac{1}{1 + \phi^2 - 2\phi cos(w)})$$ 
This is the Fourier transform of the model. 