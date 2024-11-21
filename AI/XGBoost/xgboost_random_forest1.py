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
display(data_.info())
data_['nac'] = y
data_=data_.dropna()
y=data_['nac']
data_=data_.drop(['nac'],axis=1)
print(data_.info(),len(y))

xgb.set_config(verbosity=0)
gkf = GroupKFold(n_splits=8)

groups = data_['remainder__provincia_nombre']

# Original training parameters
params_ = {
    "max_depth": 14,
    "subsample": 1,    # Use 80% of rows per tree
    "enable_categorical": True,
    "min_split_loss": 0.01,
    "objective": "reg:squarederror",
    "eta": 0.05,
    "min_samples_split": 98,
    "min_samples_leaf": 98
}

# Pruning parameters
prune_params = {
    "process_type": "update",
    "updater": "prune",
    "enable_categorical": True,
    "max_depth": 39,  # Reduced depth after pruning
    "min_split_loss": 0.01,  # Minimum gain for splitting (gamma)
    "objective": "reg:squaredlogerror",
    "eta": 0.05,
}

for i, (train_idx, test_idx) in enumerate(gkf.split(data_, y, groups)):
    if i == 0:

      # Split data into training and validation sets
      X_train, X_val = data_.iloc[train_idx], data_.iloc[test_idx]
      y_train, y_val = y.iloc[train_idx], y.iloc[test_idx]

      # Create DMatrix
      dtrain = xgb.DMatrix(X_train, label=y_train, enable_categorical=True)
      dval = xgb.DMatrix(X_val, label=y_val, enable_categorical=True)

      evals = [(dtrain, "train"), (dval, "eval")]

      # Set up interaction constraints (if required)
      params = params_.copy()
      params['interaction_constraints'] = [['number__anio', 'remainder__poblacion_total']]

      # Train the initial model
      model = xgb.train(
          params,
          dtrain,
          num_boost_round=55000,
          evals=evals,
          early_stopping_rounds=400
      )

      # Prune the model after training
      prune_model = xgb.train(
                {**params, **prune_params},  # Combine original and pruning parameters
                dtrain,
                num_boost_round=1500,  # Use the number of iterations from the previous model
                evals=evals,
                xgb_model=model
            )

      # Evaluate the pruned model
      y_pred = model.predict(dval)

      # Store results
      data_test = X_val.copy()
      data_test['target'] = y_val  # Add actual values
      data_test['predicted'] = y_pred

      print("Fold Results:")
      mse = np.mean(np.square(y_val - y_pred))  # Mean Squared Error
      r2 = 1 - (np.sum(np.square(y_val - y_pred)) / np.sum(np.square(y_val - np.mean(y_val))))  # R-squared
      print(f"Mean Squared Error: {mse}")
      print(f"R-squared: {r2}")
      break


data_test = X_val.copy()  # Use the validation set X_val
data_test['target'] = y_val  # Add actual target values from y_val
data_test['predicted'] = y_pred  # Add predicted values

data_test = data_test[data_test['remainder__provincia_nombre'].notna()]  # Ensure no NaNs or unwanted labels

# Evaluationnac
r2 = r2_score(y_val, y_pred)
mse = mean_squared_error(y_val, y_pred)

print(f"R-squared: {r2:.3f}")
print(f"Mean Squared Error: {mse:.3f}")
print(model.save_config())

attributes = model.attributes()

import matplotlib.pyplot as plt
import matplotlib.cm as cm

provinces = data_test['remainder__provincia_nombre'].unique()

plt.figure(figsize=(22, 12))
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# List of departments (or provincias) and their year-lapse
departments = data_test['remainder__departamento_nombre'].unique()

# Define a color map with a limited number of colors (5 distinct references)
cmap = plt.get_cmap("tab10")  # A qualitative colormap with 10 colors
num_colors = min(5, len(departments))  # Limit to 5 colors max
colors = [cmap(i / num_colors) for i in range(num_colors)]  # Pick first 'num_colors' colors

# Create a mapping for each department to a color
department_colors = {dep: colors[i % num_colors] for i, dep in enumerate(departments)}

# List to collect handles and labels for the legend
handles = []
labels = []

# Scatter plot: Actual values (target) with colors based on 'remainder__departamento_nombre'
for department in departments:
    # Filter the data for each department
    department_data = data_test[data_test['remainder__departamento_nombre'] == department]

    # Get the color for this department
    color = department_colors[department]

    # Plot the actual values (target)
    scatter = plt.scatter(
        department_data['remainder__poblacion_total'],
        department_data['target'],
        label=f"{department} (2012-2022)",  # Add department and year-lapse to the label
        s=100,  # Size of the scatter points
        edgecolors='k',  # Black edge around points
        alpha=0.7,  # Transparency for better visibility
        color=color  # Set color by department
    )
    # Append the handle and label for the legend
    handles.append(scatter)
    labels.append(f"{department} (2012-2022)")

# Line plot: Predicted values with the same color for consistency
for department in departments:
    # Filter the data for each department
    department_data = data_test[data_test['remainder__departamento_nombre'] == department]

    # Get the color for this department
    color = department_colors[department]

    # Sort by 'remainder__poblacion_total' for smooth line plotting
    department_data_sorted = department_data.sort_values('remainder__poblacion_total')

    # Plot predicted values
    plt.plot(
        department_data_sorted['remainder__poblacion_total'],
        department_data_sorted['predicted'],
        label=f"{department} (2012-2022)",  # Same department and year-lapse label
        linewidth=2,
        color=color  # Set color by department
    )

# Limit the legend to 5 references for compactness (Show only 5 distinct departments)
handles = handles[:8]  # Keep only the first 5 handles
labels = labels[:8]    # Keep only the first 5 labels

# Update legend with compact labels
plt.legend(handles, labels, title='Municipio por decada', loc='upper left', fontsize=12)

# Add labels and title
plt.title("Caida de nacimientos por municipio en Buenos Aires (2012-2022)", fontsize=16)
plt.xlabel("Logaritmo- Población Total", fontsize=14)
plt.ylabel("Logaritmo- Nacimientos por partido", fontsize=14)

plt.show()
X_val['predicted'] = y_pred  # Add the predicted values to the validation set

data_test['target_exp'] = np.exp(data_test['target'])
data_test['predicted_exp'] = np.exp(data_test['predicted'])

# Group by 'anio' and calculate the sum of the transformed target and predicted values
actual_sum_by_year = data_test.groupby('number__anio')['target_exp'].sum()
predicted_sum_by_year = data_test.groupby('number__anio')['predicted_exp'].sum()

# Step 2: Plot the actual vs predicted sums over time (years)
plt.figure(figsize=(10, 6))

# Plot actual vs predicted sums
plt.plot(actual_sum_by_year.index, actual_sum_by_year, label='Cantidad-nacimientos brutos', marker='x', color='r', linestyle='--', linewidth=2)
plt.plot(predicted_sum_by_year.index, predicted_sum_by_year, label='modelo', marker='o', color='b', linestyle='-', linewidth=2)

# Add labels and title
plt.title("Provincia de Buenos Aires")
plt.xlabel("Año")
plt.ylabel("Suma de nacimientos en provincia")
plt.legend()

# Display the plot
plt.show()
