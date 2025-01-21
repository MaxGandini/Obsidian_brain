#### INSERT [[PostgreSQL]] Example:

Insert data into a table:

```python
Copy code
cursor.execute("INSERT INTO your_table_name (column1, column2) VALUES (%s, %s);", (value1, value2))
connection.commit()  # Commit the transaction
```