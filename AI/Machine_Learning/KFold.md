
```
Fold
class sklearn.model_selection.KFold(n_splits=5, *, shuffle=False, random_state=None)
K-Fold cross-validator.

Provides train/test indices to split data in train/test sets. Split dataset into k consecutive folds (without shuffling by default).

Each fold is then used once as a validation while the k - 1 remaining folds form the training set.

Read more in the User Guide.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to Visualizing cross-validation behavior in scikit-learn

Parameters:
n_splitsint, default=5
Number of folds. Must be at least 2.

Changed in version 0.22: n_splits default value changed from 3 to 5.

shufflebool, default=False
Whether to shuffle the data before splitting into batches. Note that the samples within each split will not be shuffled.

random_stateint, RandomState instance or None, default=None
When shuffle is True, random_state affects the ordering of the indices, which controls the randomness of each fold. Otherwise, this parameter has no effect. Pass an int for reproducible output across multiple function calls. See Glossary.
```

In sci-kit learn, the kfold function takes an additional parameter: shuffle = Boolean

The difference is that one splits the dataset in k parts. While the shuffle parameter may divide the dataset into groups which have a non null intersection.

## GroupKFold

This method sub-divides the KFolds into the different groups of the Dataframe.
```
GroupKFold
class sklearn.model_selection.GroupKFold(n_splits=5)[source]
K-fold iterator variant with non-overlapping groups.

Each group will appear exactly once in the test set across all folds (the number of distinct groups has to be at least equal to the number of folds).

The folds are approximately balanced in the sense that the number of samples is approximately the same in each test fold.

Read more in the User Guide.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to Visualizing cross-validation behavior in scikit-learn

Parameters:
n_splitsint, default=5
Number of folds. Must be at least 2.

Changed in version 0.22: n_splits default value changed from 3 to 5.
```

## StratifiedKFold

```
GroupShuffleSplit
class sklearn.model_selection.GroupShuffleSplit(n_splits=5, *, test_size=None, train_size=None, random_state=None)[source]
Shuffle-Group(s)-Out cross-validation iterator.

Provides randomized train/test indices to split data according to a third-party provided group. This group information can be used to encode arbitrary domain specific stratifications of the samples as integers.

For instance the groups could be the year of collection of the samples and thus allow for cross-validation against time-based splits.

The difference between LeavePGroupsOut and GroupShuffleSplit is that the former generates splits using all subsets of size p unique groups, whereas GroupShuffleSplit generates a user-determined number of random test splits, each with a user-determined fraction of unique groups.

For example, a less computationally intensive alternative to LeavePGroupsOut(p=10) would be GroupShuffleSplit(test_size=10, n_splits=100).

Contrary to other cross-validation strategies, the random splits do not guarantee that test sets across all folds will be mutually exclusive, and might include overlapping samples. However, this is still very likely for sizeable datasets.

Note: The parameters test_size and train_size refer to groups, and not to samples as in ShuffleSplit.

Read more in the User Guide.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to Visualizing cross-validation behavior in scikit-learn

Parameters
:
n_splits
int, default=5
Number of re-shuffling & splitting iterations.

test_size
float, int, default=None
If float, should be between 0.0 and 1.0 and represent the proportion of groups to include in the test split (rounded up). If int, represents the absolute number of test groups. If None, the value is set to the complement of the train size. If train_size is also None, it will be set to 0.2.

train_size
float or int, default=None
If float, should be between 0.0 and 1.0 and represent the proportion of the groups to include in the train split. If int, represents the absolute number of train groups. If None, the value is automatically set to the complement of the test size.

random_state
int, RandomState instance or None, default=None
Controls the randomness of the training and testing indices produced. Pass an int for reproducible output across multiple function calls. See Glossary.
```

This method ensures that the [[KFold]] is applied to every class separately. 