to login to a database:

```sql
psql -U your_username -d your_database_name
```
### Interacting with SQL Mode

Once you're in SQL mode (`psql`), you can run SQL commands directly. Some useful commands include:

- **List all databases**:
  ```sql
  \l
  ```
  
- Switch to another database:
```
\c your_database_name
```
- List all tables:

```
sql
\dt
```
- Describe a table's structure:

```
sql
\d your_table_name
```
- Run a SQL query: For example, to query all rows from a table:

```
sql
SELECT * FROM your_table_name;
```
- Exit SQL mode: To exit psql, type:

```
sql
\q
```