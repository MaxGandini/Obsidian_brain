import urllib.request
from pathlib import Path

import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('housing_data', path='https://www.kaggle.com/datasets/camnugent/california-housing-prices/download?datasetVersionNumber=1', unzip=True)
