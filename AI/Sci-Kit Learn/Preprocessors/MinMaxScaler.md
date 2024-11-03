Examples:
- [[logistic_regression.py]]

Used to normalize numeric variables in a Dataframe. Most ML models need some sort of scaler for their inputs, because the model itself will prioritize variables with big values. 
$$x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}} \cdot (b - a) + a$$
with $a$ and $b$ , 0 and 1 respectively for standart minmax scaling.

```
class sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1), *, copy=True, clip=False)
Transform features by scaling each feature to a given range.

This estimator scales and translates each feature individually such that it is in the given range on the training set, e.g. between zero and one.

The transformation is given by:
```

an example of usage can be found in [[Logistic Regression]].
