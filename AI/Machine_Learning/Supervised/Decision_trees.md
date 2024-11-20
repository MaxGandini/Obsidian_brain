---
id: Decision trees
aliases: []
tags: []
---


![[decision_tree.png]]

It works by splitting the data into subsets based on features values yo make predictions in a tree like structure.

It has a root node, which would be the top of the tree, and it represents the initial state of the input dataset.

It has internal nodes that represent decisions and branches which represent typical decision paths. Finally, it has leaf nodes, which represent the output of the model.

Algorithm:

- Splits the data recursively based on conditions on features. The goal is maximizing the purity of the resulting subsets
- It needs a stopping criteria:
	maximum depth of tree
	minimum number of samples in a node
	node purity: it contains samples of only one class.
- Prediction:
	when the model is [[Classification]] , a sample follows the branches based on the features and eventually reaches a leaf.
	When doing [[Regression]] the predicted value is the average of the target variable in the leaf node.

Typical splitting criteria are:

- [[Classification]] : 
	gini impurity
	Entropy
- [[Regression]] : 
	[[MSE]]
	Variance Reduction


### Comparison of MSE and Variance Reduction

- **MSE** directly minimizes prediction error, commonly used in algorithms like CART (Classification and Regression Trees).
- **Variance reduction** is more intuitive, reflecting the homogeneity of subsets. It is mathematically equivalent to MSE in many cases.

Both criteria aim to create subsets that are more "pure" in terms of target values, leading to better predictions.

### Variance Reduction

Variance reduction evaluates how much the variance of the target variable decreases after a split. Lower variance in subsets indicates more homogeneous groups.

The variance at a node is:

$$
\text{Var} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \bar{y})^2
$$

For a split, the weighted average variance is:

$$
\text{Var}_{\text{split}} = \frac{|S_1|}{N} \cdot \text{Var}_{S_1} + \frac{|S_2|}{N} \cdot \text{Var}_{S_2}
$$

Variance reduction is calculated as:

$$
\text{Variance Reduction} = \text{Var}_{\text{parent}} - \text{Var}_{\text{split}}
$$

The goal is to maximize variance reduction.
