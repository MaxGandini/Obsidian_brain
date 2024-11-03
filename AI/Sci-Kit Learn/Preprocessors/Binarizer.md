It's used to transform features to binary values. Given a certain threshold, it will round up the numeric value to either a 0 or a 1.

```
class sklearn.preprocessing.Binarizer(*, threshold=0.0, copy=True)
Binarize data (set feature values to 0 or 1) according to a threshold.

Values greater than the threshold map to 1, while values less than or equal to the threshold map to 0. With the default threshold of 0, only positive values map to 1.

Binarization is a common operation on text count data where the analyst can decide to only consider the presence or absence of a feature rather than a quantified number of occurrences for instance.

It can also be used as a pre-processing step for estimators that consider boolean random variables (e.g. modelled using the Bernoulli distribution in a Bayesian setting).
```
