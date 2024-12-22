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

from sklearn.model_selection import KFold

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import r2_score

# Define hyperparameter grid
param_grid = {
    'n_estimators': [700,1000,2000,3000],
    'max_depth': [1,2,3]
              }

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data_, y_, test_size=0.2, random_state=42)

# Initialize the model
regr = RandomForestRegressor()

# Perform grid search with cross-validation
grid_search = GridSearchCV(estimator=regr, param_grid=param_grid, cv=5, scoring='r2')
grid_search.fit(X_train, y_train)

# Get best parameters and score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print(f"Best Hyperparameters: {best_params}")
print(f"Best Cross-Validation Score: {best_score}")

# Train the final model with best parameters
final_model = RandomForestRegressor(**best_params)
final_model.fit(X_train, y_train)
# Initialize StratifiedKFold

prediction = final_model.predict(X_test)
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
