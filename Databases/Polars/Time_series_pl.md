Polars has support for [[Time Series]] operations . Next are some examples for managing and filtering:
#### Time window filtering:

```python
import polars as pl
from datetime import datetime

df = pl.read_csv("docs/assets/data/apple_stock.csv", try_parse_dates=True)
print(df)
filtered_range_df = df.filter(
    pl.col("Date").is_between(datetime(1995, 7, 1), datetime(1995, 11, 1)),
)
```

#### Aggregation by year mean :

```python 
annual_average_df = df.group_by_dynamic("Date", every="1y").agg(pl.col("Close").mean())

df_with_year = annual_average_df.with_columns(pl.col("Date").dt.year().alias("year"))
print(df_with_year)
```

