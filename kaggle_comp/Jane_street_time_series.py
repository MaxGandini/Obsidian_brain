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

plt.plot(data['time_id'],data['feature_00'])
plt.show()
