
A good estimator for the correct hyperparameter, is varying it's value and fitting it to train and test data. 
As we augment the number of degrees of freedom, we should see the train score get better (marginally), but after some point k_ideal . One should see that the test score doesn't change (When evaluating it with RMSE for example).

![[Hyper_val.png]]

Around that number of degrees of freedom, we have the ideal k degrees.
