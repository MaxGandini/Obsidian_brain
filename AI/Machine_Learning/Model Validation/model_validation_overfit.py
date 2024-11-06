import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

rng = np.random.default_rng(1)

# Generar datos (polinomio de grado 1)
df = pd.DataFrame({"x": np.arange(14)})
df["y"] = 2 * df["x"] + 1 + rng.normal(size=len(df))

# Features y targets
features = ["x"]
targets = "y"

# Crear modelo (polinomio de grado 5)
model = Pipeline(
    [
        ("polynomial", PolynomialFeatures(degree=5)),
        ("regression", LinearRegression()),
    ]
)

# Dividir en train-test
df_train, df_test = train_test_split(df, train_size=0.5, random_state=1)

# Entrenar modelo
model.fit(df_train[features], df_train[targets])

# Evaluar score
print("Train score:", model.score(df_train[features], df_train[targets]))
print(" Test score:", model.score(df_test[features], df_test[targets]))

import matplotlib.pyplot as plt 
from matplotlib.figure import Figure
import seaborn
import seaborn.objects as so

# Predecir con el modelo
df = pd.concat(
    [
        df_train.assign(split="train"),
        df_test.assign(split="test"),
    ]
)
df["y_pred"] = model.predict(df[features])

# Evaluar modelo en más puntos
df_eval = pd.DataFrame({"x": np.linspace(df["x"].min(), df["x"].max(), 1000)})
df_eval["y"] = model.predict(df_eval)

seaborn.set_theme()
fig, axes = plt.subplots() 
# Graficar
seaborn.set_theme()
(
    so.Plot(df, x="x", color="split")
    .add(so.Dot(pointsize=8), y="y", label="Medición")
    .add(so.Dots(pointsize=8), y="y_pred", label="Predicción")
    .on(axes)
    .plot()
)
(
    so.Plot(df_eval, x="x", y="y")
    .add(so.Line(linestyle="--"))
    .on(axes)
    .plot()
)
plt.show()
