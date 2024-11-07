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
y = data[target]

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler

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

X_train, y_train, X_test, y_test = test_train_split()
model = LinearRegression()
model.fit(data_, y)
df["predicted"] = model.predict(data_)

(
    so.Plot(df, x="Study Hours")
    .add(so.Line(), y="predicted", label="predicted")
    .add(so.Dot(), y="Grade", label="Grade")
    .label(y="Grade")
    .show()
)
display(df)
