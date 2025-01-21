#### UPDATE [[PostgreSQL]] Example:

Update data in a table:

```python
cursor.execute("UPDATE your_table_name SET column1 = %s WHERE column2 = %s;", (new_value, condition))
connection.commit()
```

```SQL
UPDATE employees
SET salary = salary * 1.10  -- Increase salary by 10%
WHERE department = 'HR';
```
