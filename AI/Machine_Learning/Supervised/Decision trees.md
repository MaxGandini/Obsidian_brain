It's a [[Machine Learning]] alhorithm used for the classification and regression tasks. It is a [[Supervised-Learning]] model as it requires labeled data. 

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
	MSE 
	Variance Reduction

