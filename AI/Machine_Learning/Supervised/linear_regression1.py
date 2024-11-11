import kagglehub

# Download latest version
# path = kagglehub.dataset_download("yasserh/housing-prices-dataset")

# print("Path to dataset files:", path)
import pandas as pd 

data = pd.read_csv('/home/Xilian/.cache/kagglehub/datasets/yasserh/housing-prices-dataset/versions/1/Housing.csv')

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

from sklearn.linear_model import Ridge

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

param_grid = {
    'alpha': [1,2.2,2.5,2.8,3,3.2,3.6],  # List of values to search over
}

X_train , X_test, y_train, y_test = train_test_split(data_,y,test_size=0.20)

model = Ridge(alpha=10)

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='r2')

grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
best_score = grid_search.best_score_

print(f"Best Hyperparameters: {best_params}")
print(f"Best Cross-Validation Score: {best_score}")

model_fit = model.fit(X_train,y_train)

prediction = model.predict(X_test)
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

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, prediction)
print(f"Mean Absolute Error: {mae}")

from sklearn.metrics import r2_score
r2 = r2_score(y_test, prediction)
print(f"R-squared: {r2}")
