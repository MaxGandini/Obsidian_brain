import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import pandas as pd
from sklearn.utils import shuffle

# Safely determine the grandparent directory
try:
    grandparent_dir = Path(__file__).parents[2]
except NameError:
    # Fallback for interactive environments
    grandparent_dir = Path.cwd()

data_path = grandparent_dir / "datasets" / "part-0.parquet"

if 'data' in locals() and isinstance(data, pd.DataFrame):
    print("DataFrame is already loaded. Proceeding with operations...")
else:
    print("DataFrame not loaded. Loading now...")
    data = pd.read_parquet(data_path)
    print("DataFrame loaded successfully.")
# Drop columns with all nulls

columns_to_drop = [col for col in data.columns if data[col].isnull().sum() == len(data)]
data.drop(columns=columns_to_drop, inplace=True)

# Display information about remaining columns
for col in data.columns:
    print(f"Column: {col}, Nulls: {data[col].isnull().sum()}, Unique Values: {data[col].unique()}")

start_index = 0
end_index = 1000

subset_data = data.iloc[start_index:end_index]
feature='feature_64'

# Plot the sampled data
if 'time_id' in subset_data.columns and feature in subset_data.columns:
    subset_data.plot(x='time_id', y=feature, kind='scatter')
    plt.title('time_id')
    plt.xlabel("Time ID")
    plt.ylabel(feature)
    
    subset_data.plot(x='date_id', y=feature, kind='scatter')

    plt.title('date_id')
    plt.xlabel("Time ID")
    plt.ylabel(feature)
    plt.show()
else:
    print("Columns 'time_id' or 'feature_15' are not in the DataFrame.")


if 'time_id' in subset_data.columns and feature in subset_data.columns:
    subset_data.plot(x='time_id', y='responder_0', kind='scatter')
    plt.title('responder_0')
    plt.xlabel("Time ID")
    plt.ylabel(feature)
    subset_data.plot(x='time_id', y='responder_8', kind='scatter')
    plt.title('responder_8')
    plt.xlabel("Time ID")
    plt.ylabel(feature)
    plt.show()
else:
    print("Columns 'time_id' or 'feature_15' are not in the DataFrame.")

