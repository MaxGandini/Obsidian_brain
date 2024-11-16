
mport kagglehub

# Download latest version
# path = kagglehub.dataset_download("yasserh/housing-prices-dataset")
# print("Path to dataset files:", path)

import pandas as pd 
from pathlib import Path

grandparent_dir= Path(__file__).parents[4]

data_path = grandparent_dir / "datasets" / "Housing.csv"

data = pd.read_csv(data_path)

import pandas as pd
import seaborn.objects as so
import sklearn
import matplotlib.pyplot as plt

sklearn.set_config(transform_output="pandas")
target = "price"  

X = data.drop(target,axis=1)

y_ = data[[target]]

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(y_)
y = scaler.transform(y_)

transformer = ColumnTransformer(
    [
        (
            "category", 
            OrdinalEncoder(),
            ["mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea","furnishingstatus"],  
        ),
        (
            "number",
            MinMaxScaler(),
            ["bedrooms","stories","bathrooms","parking"],
        )
    ],
    remainder="passthrough",
    #verbose_feature_names_out=True,
)


data_= pd.DataFrame(transformer.fit_transform(X), columns=transformer.get_feature_names_out())

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold


# Initialize StratifiedKFold
regr = RandomForestRegressor()


param_grid = {
    'n_estimators': [700,800],  # List of values to search over
    'n_jobs': [None,1],  # List of values to search over
    'max_depth': [1,2,3]

}

kf = KFold(n_splits=5, shuffle=True)

# Generate splits and create train/test sets
for train_index, test_index in kf.split(X, y):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    X_train , X_test, y_train, y_test = train_test_split(data_,y,test_size=0.20)

    regr.fit(X_train, y_train)

    grid_search = GridSearchCV(estimator=regr, param_grid=param_grid, cv=5, scoring='r2')

    grid_search.fit(X_train, y_train)

    best_params = grid_search.best_params_
    best_score = grid_search.best_score_

    print(f"Best Hyperparameters: {best_params}")
    print(f"Best Cross-Validation Score: {best_score}")

regr.fit(**best_params)

prediction = regr.predict(X_test)
data_test = X_test
data_test['target'] = y_test

data_test['predicted'] = prediction

(
    so.Plot(data_test, x="remainder__area")
    .add(so.Line(), y="predicted", label="predicted")
    .add(so.Dot(), y="target", label="target")
    .label(y="target")
    .show()
)
display(data_)

from sklearn.metrics import mean_squared_error
mae = mean_squared_error(y_test, prediction)
print(f"Mean squared Error: {mae}")

from sklearn.metrics import r2_score
r2 = r2_score(y_test, prediction)
print(f"R-squared: {r2}")
