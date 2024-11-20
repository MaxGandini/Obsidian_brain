Entropy is a measure of uncertainty or the average amount of information produced by a stochastic source of data. In information theory, the entropy $H$ of a discrete random variable $X$ with possible outcomes $\{x_1, x_2, \dots, x_n\}$ and a probability mass function $P(X)$ is defined as:

$$
H(X) = - \sum_{i=1}^{n} P(x_i) \log_b P(x_i)
$$

- $H(X)$: Entropy of the random variable $X$.
- $P(x_i)$: Probability of the $i$-th outcome.
- $b$: Base of the logarithm (commonly 2 for bits or natural logarithm $e$ for nats).

**Explanation**:
- If all outcomes are equally likely, the entropy is maximized, indicating the greatest uncertainty.
- If one outcome is certain, entropy is zero, reflecting no uncertainty.
- The choice of the logarithm base determines the unit of entropy:
  - Base 2 ($b=2$): Entropy is measured in bits.
  - Base $e$: Entropy is measured in nats.