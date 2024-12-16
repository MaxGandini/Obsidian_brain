import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import pandas as pd 

grandparent_dir= Path(__file__).parents[2]

data_path = grandparent_dir / "datasets" / "part-0.parquet"
data = pd.read_parquet(data_path)

import sklearn
import matplotlib.pyplot as plt

for row in data.columns.tolist():  # Use .tolist() to work with a static list of columns
    if data[row].isnull().sum() == 1944210:  # Access the column directly by its name
        data.drop(columns=[row], inplace=True)  # Drop the column if the condition is met
    else:
        pass
    # Only print if the column still exists in the DataFrame
    if row in data.columns:
        print(row,data[row].isnull().sum(),data[row].unique())
# Take a random sample of 1000 rows
subset_data = data.iloc[:1000]
# Plot the sampled data
subset_data.plot(x='time_id', y='feature_15', kind='scatter')

plt.show()
