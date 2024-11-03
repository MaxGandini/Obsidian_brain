import urllib.request
from pathlib import Path

import pandas as pd
import seaborn.objects as so
import sklearn

sklearn.set_config(transform_output="pandas")
from pathlib import Path
import urllib.request

def download(url: str, destination_folder: Path) -> Path:
    """
    Downloads a file from an URL and returns a path to the new file.
    It also checks if the file already exists and doesn't do anything if there is no file
    """
    destination_folder.mkdir(parents=True, exist_ok=True)

    filename = Path(url).name
    path = destination_folder / filename

    if not path.exists():
        urllib.request.urlretrieve(url, path)

    return path
