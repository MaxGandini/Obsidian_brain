import urllib.request
from pathlib import Path

import pandas as pd
import seaborn.objects as so
import sklearn

sklearn.set_config(transform_output="pandas")

def download(url: str, /) -> Path:
    """
    Downloads the url and gives the path 
    to the file.
    """
    filename = Path(url).name
    path = Path(filename)
    if not path.exists():
        urllib.request.urlretrieve(url, path)
    return path

download
