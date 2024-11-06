import kagglehub

# Download latest version
# path = kagglehub.dataset_download("yasserh/housing-prices-dataset")

# print("Path to dataset files:", path)
import pandas as pd 

data = pd.read_csv('/home/Xilian/.cache/kagglehub/datasets/yasserh/housing-prices-dataset/versions/1/Housing.csv')


