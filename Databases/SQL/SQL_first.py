import psycopg2
import os

from pathlib import Path

grandparent_dir= Path(__file__).parents[3]

data_path = grandparent_dir / "datasets" / "Housing.csv"

