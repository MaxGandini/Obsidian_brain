An instance of [[Cross Validation]]. Uses a sequence of test_train splits one after the other similarly to how a time series is constructed in time.

```
TimeSeriesSplit
class sklearn.model_selection.TimeSeriesSplit(n_splits=5, *, max_train_size=None, test_size=None, gap=0)
Time Series cross-validator.

Provides train/test indices to split time series data samples that are observed at fixed time intervals, in train/test sets. In each split, test indices must be higher than before, and thus shuffling in cross validator is inappropriate.

This cross-validation object is a variation of KFold. In the kth split, it returns first k folds as train set and the (k+1)th fold as test set.

Note that unlike standard cross-validation methods, successive training sets are supersets of those that come before them.

Read more in the User Guide.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to Visualizing cross-validation behavior in scikit-learn

Parameters:
n_splitsint, default=5
Number of splits. Must be at least 2.

max_train_sizeint, default=None
Maximum size for a single training set.

test_sizeint, default=None
Used to limit the size of the test set. Defaults to n_samples // (n_splits + 1), which is the maximum allowed value with gap=0.

gapint, default=0
Number of samples to exclude from the end of each train set before the test set.
```
