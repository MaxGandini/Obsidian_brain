#### SELECT [[PostgreSQL]] Example:

Fetch all rows from a table:

``` python

cursor.execute("SELECT * FROM your_table_name;") rows = cursor.fetchall() for row in rows:     print(row)
```

```SQL
SELECT * FROM employees;  -- Select all columns
SELECT name, salary FROM employees WHERE department = 'Engineering';
```
