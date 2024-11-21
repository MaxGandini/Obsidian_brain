---
id: MSE
aliases: []
tags: []
---

MSE measures the average squared difference between predicted and actual values. It evaluates the quality of a split by minimizing the prediction error.

The formula for MSE at a node is:

$$
\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \bar{y})^2
$$

Where:
- $y_i$: Actual value of the $i$-th data point.
- $\bar{y}$: Mean of the target variable values in the node.
- $N$: Number of data points in the node.

For a given split, the weighted average MSE is:

$$
\text{MSE}_{\text{split}} = \frac{|S_1|}{N} \cdot \text{MSE}_{S_1} + \frac{|S_2|}{N} \cdot \text{MSE}_{S_2}
$$

The goal is to minimize $\text{MSE}_{\text{split}}$.

