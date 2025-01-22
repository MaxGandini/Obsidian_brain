SQL is a structured query language. It's the standard to manage and manipulate relational databases. 
It is used to create, read, update and delete data in a database.

![[sql.png]]

Key operations:

Some examples of these operations will be made considering :
```SQL
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    salary NUMERIC(10, 2),
    hire_date DATE
);
```

```SQL
CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
);
```

Which is an example for creating a table of employees.

- [[SELECT]]
- [[INSERT]]
- [[UPDATE]]
- [[DELETE]]
- [[CREATE]]
- [[DROP]]
- [[JOIN]]
- [[AGGREGATE]]
- [[TRANSACTIONS]]

In many cases, SQL is embedded within or used alongside a general-purpose programming language like [[Python]]. This is achieved with libraries like [[BigQuery]] or [[SQLITE]] for local databases.

