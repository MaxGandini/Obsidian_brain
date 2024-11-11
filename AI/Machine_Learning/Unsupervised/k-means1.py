import pandas as pd 
from pathlib import Path

grandparent_dir= Path(__file__).parents[4]

data_path = grandparent_dir / "datasets" / "Wholesale_customers_data.csv"

data = pd.read_csv(data_path)
