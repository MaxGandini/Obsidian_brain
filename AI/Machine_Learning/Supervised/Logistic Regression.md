A logistic model is a statistical model that takes into account the logarithmic probabilities of an event as a linear combination of one or more independent variables. 
Simplistic example for logreg: [[logistic_regression.py]]

![[logistc.png]]
The formula for the probability of the linear combination of events is given by: 

$$\log \left( \frac{P(y = 1 | X)}{1 - P(y = 1 | X)} \right) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n$$

The expression for the probability is easily obtainable and with respect to a variable X, it look like the image above.
In machine learning this is a useful way of training a model to predict a boolean variable with a certain probability given some features X. 

![[logreg_result.png]]

This is the result of the simplistic model above. For this, we used an instance of [[Preprocessor]] in [[Sci-Kit Learn]] . 