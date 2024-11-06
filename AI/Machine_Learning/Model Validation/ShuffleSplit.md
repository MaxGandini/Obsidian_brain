An instance of [[Cross Validation]]. Given a set of parameters divides subgroups which are shuffled in the dataset in train_test splits.

```
class sklearn.model_selection.ShuffleSplit(n_splits=10, *, test_size=None, train_size=None, random_state=None)
Random permutation cross-validator.

Yields indices to split data into training and test sets.

Note: contrary to other cross-validation strategies, random splits do not guarantee that test sets across all folds will be mutually exclusive, and might include overlapping samples. However, this is still very likely for sizeable datasets.

Read more in the User Guide.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to Visualizing cross-validation behavior in scikit-learn

Parameters:
n_splits
int, default=10
Number of re-shuffling & splitting iterations.

test_size
float or int, default=None
If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. If int, represents the absolute number of test samples. If None, the value is set to the complement of the train size. If train_size is also None, it will be set to 0.1.

train_size
float or int, default=None
If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split. If int, represents the absolute number of train samples. If None, the value is automatically set to the complement of the test size.

random_state
int, RandomState instance or None, default=None
Controls the randomness of the training and testing indices produced. Pass an int for reproducible output across multiple function calls. See Glossary.
```