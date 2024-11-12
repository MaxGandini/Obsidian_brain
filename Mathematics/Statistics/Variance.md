Variance measures the model's sensitivity to fluctuations in the training dataset. High variance indicates that the model is highly sensitive to the specific dataset used and may perform poorly on new data.

High variance leads to overfitting, where the model captures noise in the training data as if it were true patterns.

Mathematically, variance is defined as the expected variability of the predictions around the mean prediction:

$$ \text{Variance} = \mathbb{E}[(\hat{y} - \mathbb{E}[\hat{y}])^2] $$
