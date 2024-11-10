#### SELECT [[PostgreSQL]] Example:

Fetch all rows from a table:

``` python

cursor.execute("SELECT * FROM your_table_name;") rows = cursor.fetchall() for row in rows:     print(row)
```
