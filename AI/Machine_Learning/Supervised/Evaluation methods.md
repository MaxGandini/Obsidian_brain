## Confusion Matrix

The confusion matrix is a quick way to graphically get a sense of how well a model is doing. 

Similar concepts can be found in [[Model Validation]] for more in depth mathematical look.

![[conf.png]]
It doesn't get simpler than what is show in the image, if you have a classification model that attempts to predict a boolean, the matrix should be dominant in its diagonal to have a robust performance.

There are many ways of interpreting this matrix, because one can have many sub-measures that indicate qualities of the model: 

- $Accuracy = \frac{True True + False False}{All Perm}$
- $Precision = \frac{True True}{True False + True True}$
- $Recall = \frac {True True} {True True + False True}$

these metrics are also explained in [[Model Validation]].