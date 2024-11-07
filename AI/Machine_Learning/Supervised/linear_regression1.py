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
            ["bedrooms","stories","bathrooms","area","parking"],
        )
    ],
    remainder="passthrough",
    #verbose_feature_names_out=True,
)


data_= pd.DataFrame(transformer.fit_transform(X), columns=transformer.get_feature_names_out())

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

X_train , X_test, y_train, y_test = train_test_split(data_,y,test_size=0.20)

model = LinearRegression()
model_fit = model.fit(X_train,y_train)
prediction = model.predict(X_test)
data_test = X_test
data_test['target'] = y_test

data_test['predicted'] = prediction

(
    so.Plot(data_test, x="number__area")
    .add(so.Line(), y="predicted", label="predicted")
    .add(so.Dot(), y="target", label="target")
    .label(y="target")
    .show()
)
display(data_)
