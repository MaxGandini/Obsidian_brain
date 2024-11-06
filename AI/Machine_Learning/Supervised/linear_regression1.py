import kagglehub

# Download latest version
try:
    path = kagglehub.dataset_download("yasserh/housing-prices-dataset")
except:
    pass

print("Path to dataset files:", path)
import pandas as pd 

data = pd.read_csv('/home/Xilian/.cache/kagglehub/datasets/yasserh/housing-prices-dataset/versions/1/Housing.csv')


