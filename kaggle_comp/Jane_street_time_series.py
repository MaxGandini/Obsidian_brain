import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import pandas as pd
from sklearn.utils import shuffle
import seaborn as sns

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
end_index = 100000

time_id_counts = data['time_id'].value_counts()

# Plot a histogram of counts
time_id_counts.plot(kind='bar')
plt.xlabel("Unique Time IDs")
plt.ylabel("Count of Repeated Values")
plt.title("Histogram of Counts for Unique Time IDs")
plt.show()

subset_data_ = data.iloc[start_index:end_index]
subset_data = subset_data_.groupby('time_id', as_index=False).sum()
feature='feature_61'

plt.figure(figsize=(8, 6))  # Set the figure size
correlation_matrix = subset_data_.corr()
plt.matshow(correlation_matrix, cmap='coolwarm', fignum=1)  # fignum=1 to use the plt.figure
plt.colorbar()  # Add colorbar for scale

# Add labels for clarity
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45, ha='left')
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

plt.title("Correlation Matrix", pad=20)  # Add a title
plt.show()
# Plot the sampled data
if 'time_id' in subset_data.columns and feature in subset_data.columns:
    subset_data.plot(x='time_id', y=feature, kind='scatter')
    plt.title('time_id')
    plt.xlabel("Time ID")
    plt.ylabel(feature)
    plt.show()
else:
    print("Columns 'time_id' or 'feature_15' are not in the DataFrame.")


if 'time_id' in subset_data.columns and feature in subset_data.columns:
    subset_data.plot(x='time_id', y='responder_6', kind='scatter')
    plt.title('responder_0')
    plt.xlabel("Time ID")
    plt.ylabel(feature)
    subset_data.plot(x='time_id', y='responder_8', kind='scatter')
    plt.title('responder_6')
    plt.xlabel("Time ID")
    plt.ylabel(feature)
    plt.show()
else:
    print("Columns 'time_id' or 'feature_15' are not in the DataFrame.")

