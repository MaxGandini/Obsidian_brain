BigQuery is a fully managed, serverless data warehouse offered by google cloud that allows you to run SQL-like queries on large datasets. 
The syntax is specific, and provides advanced functionalities such as data processing and integration with google cloud services. 

- Using SQL in BigQuery
BigQuery uses a SQL dialect called Standard SQL, which is based on the SQL 2011 specification. It provides robust SQL features, such as:

	SELECT queries for data retrieval
	JOINs (INNER, LEFT, RIGHT, etc.)
	Aggregation (GROUP BY, COUNT, SUM, AVG, etc.)
	Window Functions (e.g., ROW_NUMBER(), RANK())
	Subqueries
	Data modification (INSERT, UPDATE, DELETE)

- Connecting to BigQuery Using Python

Google provides a Python client for BigQuery (google-cloud-bigquery) that allows you to interact with BigQuery using SQL commands in your Python code.

From the kaggle course:

```python
from google.cloud import bigquery

client = bigquery.Client()
dataset_ref = client.dataset('hacker_news', project='bigquery-public-data')
dataset = client.get_dataset(dataset_ref)
```

This is a typical definition of a client, a reference and the extraction of a whole dataset.
To list the tables:

```python
tables=list(client.list_tables(dataset))
for table in tables:
	print(table.table_id)
```

similarly to the dataset, we can fetch a table: ('full' is one of the table IDs)

```python
talbe_ref = dataset_ref.table('full')
table = client.get_table(table_ref)
```

A diagram of the above:
![[sql_struct.png]]
