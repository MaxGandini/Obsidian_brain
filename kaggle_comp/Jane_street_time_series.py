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


#Un poco de procesado: RECORDAR ESTO, se esta tirando mucha data.
columns_to_drop = [col for col in data.columns if data[col].isnull().sum() == len(data)]
data.drop(columns=columns_to_drop, inplace=True)
nan_counts = data.isnull().sum()

# Drop columns with more than 20,000 NaN values
threshold = 20000
columns_to_drop = nan_counts[nan_counts > threshold].index
data.drop(columns=columns_to_drop)

# Display information about remaining columns

start_index = 0
end_index = 20000

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

for col in subset_data.columns:
    print(f"Column: {col}, Nulls: {subset_data[col].isnull().sum()}, Unique Values: {subset_data[col].unique()}")

plt.figure(figsize=(8, 6))  # Set the figure size
correlation_matrix = subset_data_.corr()
plt.matshow(correlation_matrix, cmap='coolwarm', fignum=1)  # fignum=1 to use the plt.figure
plt.colorbar()  # Add colorbar for scale

# Add labels for clarity
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45, ha='left')
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

plt.title("Correlation Matrix", pad=20)  # Add a title
plt.show()
correlation_matrix = subset_data_.corr()

# Plot the correlation matrix
plt.matshow(correlation_matrix, cmap='coolwarm', fignum=1)  # fignum=1 to use the plt.figure
plt.colorbar()  # Add colorbar for scale

# Add labels for clarity
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45, ha='left')
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title("Correlation Matrix", pad=20)  # Add a title
plt.show()
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Identify pairs with high correlation
threshold = 0.9
high_corr_pairs = []

for i in range(len(correlation_matrix.columns)):
    for j in range(i + 1, len(correlation_matrix.columns)):  # Avoid duplicate pairs
        if abs(correlation_matrix.iloc[i, j]) > threshold:
            col1 = correlation_matrix.columns[i]
            col2 = correlation_matrix.columns[j]
            high_corr_pairs.append((col1, col2))

# Plot high-correlation pairs
for col1, col2 in high_corr_pairs:
    print(f"Plotting variables with high correlation: {col1} vs {col2}")
    plt.figure(figsize=(6, 4))
    plt.scatter(subset_data_[col1], subset_data_[col2], alpha=0.7)
    plt.title(f'{col1} vs {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.grid(True)
    plt.show()

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

# Define the window size (e.g., 3 for ±1 values around each point)
window_size = 40

def fill_nan_with_window_mean(column, window):
    """Fill NaN values in a column using a rolling window mean."""
    # Rolling mean with NaN values excluded
    rolling_mean = column.rolling(window=window, min_periods=1, center=True).mean()
    # Replace NaNs with the rolling mean
    return column.fillna(rolling_mean)

# Apply the function to each column
subset_data_filled = subset_data_.apply(lambda col: fill_nan_with_window_mean(col, window_size))
subset_data_filled = subset_data_filled.fillna(0)
subset_data_clean = subset_data_filled.select_dtypes(include=[np.number])

# Step 1: Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(subset_data_clean)

# Step 2: Apply PCA
n_components = min(data_scaled.shape)  # Number of components to retain
pca = PCA(n_components=n_components)
pca_result = pca.fit_transform(data_scaled)

# Step 3: Explained variance ratio
explained_variance = pca.explained_variance_ratio_

# Step 4: Plot explained variance
plt.figure(figsize=(8, 5))
plt.plot(np.cumsum(explained_variance), marker='o', linestyle='--')
plt.title('Cumulative Explained Variance')
plt.xlabel('Number of Components')
plt.ylabel('Explained Variance Ratio')
plt.grid()
plt.show()

# Step 5: Transform the dataset with selected components
# Retain enough components to explain 95% of the variance
cumulative_variance = np.cumsum(explained_variance)
n_selected_components = np.argmax(cumulative_variance >= 0.95) + 1

print(f"Number of components selected to explain 95% variance: {n_selected_components}")

pca_selected = PCA(n_components=n_selected_components)
data_pca = pca_selected.fit_transform(data_scaled)

# Optional: Create a DataFrame with PCA-transformed data
pca_df = pd.DataFrame(data_pca, columns=[f"PC{i+1}" for i in range(n_selected_components)])
print(pca_df.head())
