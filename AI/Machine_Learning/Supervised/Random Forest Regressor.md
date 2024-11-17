It's an instance of [[Decision trees]] . It is a random forest, because it's an ensemble of decision trees. Each of which is trained in a random subset of the input data.

A random subset of features is chosen, so that the diversity of trees is increased and the model's performance is optimized. 

- Pros :
	better accuracy and less overfitting as the model uses many variety's of trees. 
- Cons:
	Computationally expensive.
	Less interpretable. This is obvious because a single decision tree can be decomposed into a diagram. Imagine navigating conceptually a sea of hundreds of diagrams.

Example of usage on a birth database of Argentina:

https://colab.research.google.com/drive/1wP661vU7jTGrXOxWbBdKcfsLfttTdd8l?usp=sharing

This is an example of a dataset that has labeled subgroups. Another approach can be made to this problem, taking into account that random forests do not correct for patterns in the [[residue]] of the previous computed tree. [[XGBoost]] is another popular library which has been used in many [[kaggle]] competitions. 
