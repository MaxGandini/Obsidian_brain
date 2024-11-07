It's a method that automatically splits the dataset into train test splits. It takes the features and the target variable, it can also take random states, shuffle the splits ([[ShuffleSplit]]) and stratify it.
An example of usage can be found in [[Model Validation]].

IE:
[[linear_regression1.py]]

```
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

X_train
array([[4, 5],
       [0, 1],
       [6, 7]])
y_train
[2, 0, 3]
X_test
array([[2, 3],
       [8, 9]])
y_test
[1, 4]
```

```
train_test_split
sklearn.model_selection.train_test_split(*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None)[source]
Split arrays or matrices into random train and test subsets.

Quick utility that wraps input validation, next(ShuffleSplit().split(X, y)), and application to input data into a single call for splitting (and optionally subsampling) data into a one-liner.

Read more in the User Guide.

Parameters:
*arrays
sequence of indexables with same length / shape[0]
Allowed inputs are lists, numpy arrays, scipy-sparse matrices or pandas dataframes.

test_size
float or int, default=None
If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. If int, represents the absolute number of test samples. If None, the value is set to the complement of the train size. If train_size is also None, it will be set to 0.25.

train_size
float or int, default=None
If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the train split. If int, represents the absolute number of train samples. If None, the value is automatically set to the complement of the test size.

random_state
int, RandomState instance or None, default=None
Controls the shuffling applied to the data before applying the split. Pass an int for reproducible output across multiple function calls. See Glossary.

shuffle
bool, default=True
Whether or not to shuffle the data before splitting. If shuffle=False then stratify must be None.

stratify
array-like, default=None
If not None, data is split in a stratified fashion, using this as the class labels. Read more in the User Guide.

Returns:
splittinglist, length=2 * len(arrays)
List containing train-test split of inputs.
```