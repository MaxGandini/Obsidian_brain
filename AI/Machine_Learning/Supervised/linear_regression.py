import pandas as pd
import seaborn.objects as so
import sklearn
import matplotlib.pyplot as plt

sklearn.set_config(transform_output="pandas")
df = pd.DataFrame(
    {
        "Study Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # característic
        "Grade": [50, 55, 65, 70, 70, 75, 80, 85, 90, 95],  # objetive
    }
)
features = ["Study Hours"]  # list[str]
target = "Grade"  # str

X = df[features]  # DataFrame
y = df[target]

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
df["predicted"] = model.predict(X)
(
    so.Plot(df, x="Study Hours")
    .add(so.Line(), y="predicted", label="predicted")
    .add(so.Dot(), y="Grade", label="Grade")
    .label(y="Grade")
    .show()
)
display(df)
