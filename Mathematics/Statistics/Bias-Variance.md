The Bias-Variance trade off is a key concept in [[Model Validation]] .

[[Bias]] and [[Variance]] in [[_Index_of_Statistics]].

![[bias-var.png]]

It explains the balance between how well a model fits the training data, and how well it generalizes to new data. The overfitting model, is a model that has too much added complexity, and fitted towards data fluctuations and noise. As seen in the graph, the generalization error becomes larger after some point. 

On the other hand, we have the low complexity model, which is highly biased as it misses patterns in the data which are key for describing the phenomenon. (Underfitting)
#### Mean squared error: 

A statistical metric that takes into account both components is MSE:
$$ \text{MSE} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error} $$

![[bias-variance-target.png]]