It's a relational database system that works very well for reproducing [[BigQuery]] locally on a machine (with extensions).

From it's manual: 

```
PostgreSQL is an object-relational database management system (ORDBMS) based on [POSTGRES, Version 4.2](https://dsf.berkeley.edu/postgres.html), developed at the University of California at Berkeley Computer Science Department. POSTGRES pioneered many concepts that only became available in some commercial database systems much later.

PostgreSQL is an open-source descendant of this original Berkeley code. It supports a large part of the SQL standard and offers many modern features:
Also, PostgreSQL can be extended by the user in many ways, for example by adding new

And because of the liberal license, PostgreSQL can be used, modified, and distributed by anyone free of charge for any purpose, be it private, commercial, or academic.
```

# Using PostgreSQL with Python and psycopg2

`psycopg2` is a popular PostgreSQL adapter for Python that allows you to execute SQL queries and interact with a PostgreSQL database directly from your code.

Run the following command in your terminal to install `psycopg2`:
```bash
pip install psycopg2
```

```
import psycopg2
# Define your database connection parameters
connection = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="localhost",  # or the IP address of the database server
    port="5432"        # default PostgreSQL port
)
cursor = connection.cursor()
```

It's important to create a cursor object to use the query methods in it.

Below is a link to a python script to initiate a table and manage typical database operations.

[[SQL_database.py]]

The login is obfuscated through the [[os]] library included by [[Python]]. The aliases are defined in [[Bash]] and accessed.