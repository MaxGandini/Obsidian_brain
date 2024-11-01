## Confusion Matrix

The confusion matrix is a quick way to graphically get a sense of how well a model is doing. 
![[conf.png]]
It doesn't get simpler than what is show in the image, if you have a classification model that attempts to predict a boolean, the matrix should be dominant in its diagonal to have a robust performance.

There are many ways of interpreting this matrix, because one can have many sub-measures that indicate qualities of the model: 

- $Accuracy = \frac{True True + False False}{All Perm}$
- $Precision = \frac{True True}{True False + True True}$
- $Recall = \frac {True True} {True True + False True}$
