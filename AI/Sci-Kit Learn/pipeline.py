from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

df = pd.DataFrame(
    {
        "weight": [150, 160, 170, 180, 190],   
        "color": ["red", "red", "orange", "orange", "orange"],
        "fruit": [0, 0, 1, 1, 1],
    }
)

X = df[["weight", "color"]]
y = df["fruit"]

encoder = ColumnTransformer(
    [("category", OrdinalEncoder(), ["color"])],
    remainder="passthrough",
    verbose_feature_names_out=False,
)
pipeline = Pipeline(
    [
        ("encoder", encoder),
        ("regression", LogisticRegression()),
    ]
)

pipeline.fit(X, y)
display(pipeline)
display(pipeline.predict(X))

