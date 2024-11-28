A likelihood function measures how well a statistical model explains *observed data* by calculating the probability of seeing that data under different parameter values of the model.

It's constructed from the joint probability distribution of the random variable that presumably generated the observations.

Given a probability density or mass function $x \mapsto f(x \mid \theta)$, where $x$ is a realization of the random variable $X$, the likelihood function is $\theta \mapsto f(x \mid \theta)$, often written 
$$\mathcal{L}(\theta \mid x).$$ In other words, when $f(x \mid \theta)$ is viewed as a function of $x$ with $\theta$ fixed, it is a probability density function, and when viewed as a function of $\theta$ with $x$ fixed, it is a likelihood function. In the frequentist paradigm, the notation $f(x \mid \theta)$ is often avoided and instead $f(x; \theta)$ or $f(x, \theta)$ are used to indicate that $\theta$ is regarded as a fixed unknown quantity rather than as a random variable being conditioned on.

