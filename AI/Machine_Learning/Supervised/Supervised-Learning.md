Supervised learning is a pretty self explanatory term. You have an algorithm that is trained with input data, the input data is divided into two sections:
- x_train
- y_train
![[Supervised-Machine-Learning-Process-1536x864-1009220488.png]]

This nomenclature of x and y gives the idea that you have a certain target characteristic that you want to predict. Your y_train data is the input you have so that the algorithm is trained towards the actual patterns you are trying to predict.

After this, you have a fit, which returns the adjusted set of parameters you give to the algorithm, and a trained model which can be fed new data.

Typical examples are [[Regression]] and [[Classification]] models. Although there are many classification examples of [[Unsupervised-Learning]] .
Regression models seek to predict a continuous variable, whereas classification predicts discrete values (It can be a boolean value, up to a discretized continuous variable depending on the model).

