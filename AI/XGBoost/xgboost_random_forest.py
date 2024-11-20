import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import GroupKFold
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from pathlib import Path
import requests
import sklearn
import numpy as np
from sklearn.preprocessing import FunctionTransformer
import xgboost
import matplotlib.pyplot as plt
import seaborn as sns

proyecto="nacimientos-anio-nacion.csv"
archivo = Path(proyecto)
url = r"https://datosabiertos.renaper.gob.ar/nacimientos_por_departamento_y_anio_2012_2022.csv"
if not archivo.exists():
    r = requests.get(url,verify=False)
    archivo.write_bytes(r.content)

nacimientos_nacion=pd.read_csv(archivo)
target = "nacimientos_cantidad"

nacimientos_nacion_new = nacimientos_nacion.drop(['provincia_id','departamento_id','tbn',],axis=1)
nacimientos_nacion_new

log_scaler = FunctionTransformer(np.log1p, validate=True)

sklearn.set_config(transform_output="pandas")
target = "nacimientos_cantidad"

X = nacimientos_nacion_new.drop(target,axis=1)
y_ = nacimientos_nacion_new[[target]]

log_scaler.fit(y_)
y = log_scaler.transform(y_)
transformer = ColumnTransformer(
    [
        (
            "number",
            MinMaxScaler(),
            ["anio",],
        )
    ],
    remainder="passthrough",
    #verbose_feature_names_out=True,
)

data_= pd.DataFrame(transformer.fit_transform(X), columns=transformer.get_feature_names_out())

data_['remainder__departamento_nombre'] = data_['remainder__departamento_nombre'].astype("category")
data_['remainder__provincia_nombre'] = data_['remainder__provincia_nombre'].astype("category")

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

log_ptotal=FunctionTransformer(np.log1p, validate=True)

# Fit and transform the specified column
data_['remainder__poblacion_total'] = log_ptotal.fit_transform(
    data_['remainder__poblacion_total'].to_numpy().reshape(-1, 1)
)
X_train, X_val, y_train, y_val = train_test_split(data_, y, test_size=0.01, random_state=42)

dtrain = xgb.DMatrix(X_train, label=y_train,enable_categorical=True)
dval = xgb.DMatrix(X_val, label=y_val,enable_categorical=True)

# Initialize XGBoost model with key hyperparameters

params= {
    "max_depth": 6,
    "n_estimators": [250,300],
    "subsample": 0.8,    # Use 80% of features per tree
    "enable_categorical":True,
    "refresh_leaf":1
}

evals = [(dtrain, "train"), (dval, "eval")]

model_no_constraints = xgboost.train(params, dtrain,evals=evals,
                                 num_boost_round = 1000,
                                 early_stopping_rounds = 10)

params_constrained = params.copy()

params_constrained['interaction_constraints'] = [['number__anio','remainder__departamento_nombre','remainder__poblacion_total']]

model = xgb.train(params_constrained, dtrain, num_boost_round = 1000, evals = evals, early_stopping_rounds = 10)

num_boost_round=10

prune_params = {
"process_type": "update",
"updater": "prune",
"max_depth": 14,  # New maximum depth for pruning
"min_split_loss": 1.0,  # Equivalent to `gamma`
}

pruned_model = xgb.train(
                          params=prune_params,
                          dtrain=dtrain,
                          num_boost_round=num_boost_round,  # Must match the existing number of boosting rounds
                          evals=[(dval, "eval")],
                          verbose_eval=10,
                          xgb_model=model  # Pass the existing model to update/prune
                        )


y_pred =model.predict(dval)

data_test = X_val.copy()
data_test['target'] = y_val  # Add actual values to data_test
data_test['predicted'] = y_pred

plt.figure(figsize=(12, 8))

sns.scatterplot(
    data=data_test,
    x="remainder__poblacion_total",
    y="target",
    hue="remainder__provincia_nombre",
    label='Actual Values',
    legend=False,
    palette="viridis"
)

sns.lineplot(
    data=data_test,
    x="remainder__poblacion_total",
    y="predicted",
    hue="remainder__provincia_nombre",
    legend=False,
    palette='viridis'
)

plt.show()
# Evaluation
r2 = r2_score(y_val, y_pred)
mse = mean_squared_error(y_val, y_pred)

print(f"R-squared: {r2:.3f}")
print(f"Mean Squared Error: {mse:.3f}")
print(model.save_config())
attributes = model.attributes()

