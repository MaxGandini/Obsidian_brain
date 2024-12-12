
#### SELECT [[PostgreSQL]] Example:

Fetch all rows from a table:

``` python

cursor.execute("SELECT * FROM your_table_name;") 
rows = cursor.fetchall() 
for row in rows:     
	print(row)

```
#### SQL example:

```SQL
SELECT * FROM employees;  -- Select all columns
SELECT name, salary FROM employees WHERE department = 'Engineering';
```

##### Different operations from [[Relational algebra - SQL]] 

##### Union
```SQL
SELECT NAME FROM Students
UNION
SELECT Name FROM Teachers;
```
##### Intersection
```SQL
SELECT NAME FROM Students
INTERSECT
SELECT Name FROM Teachers;
```
##### Set difference (-)
```SQL
SELECT NAME FROM Students
EXCEPT
SELECT Name FROM Teachers;
```
###### Cartesian product
```SQL
SELECT * FROM Students, Courses;
```
