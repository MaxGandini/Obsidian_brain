
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
Will return all the names from both tables eliminating duplicates.
```SQL
SELECT NAME FROM Students
UNION
SELECT Name FROM Teachers;
```
##### Intersection
Will find rows that match and return a table with matched names.
```SQL
SELECT NAME FROM Students
INTERSECT
SELECT Name FROM Teachers;
```
##### Set difference (-)
Finds the names from Students EXCEPT the name is in Teachers.
```SQL
SELECT NAME FROM Students
EXCEPT
SELECT Name FROM Teachers;
```
###### Cartesian product
This will create a new result with all possible combinations of rows from the students and courses table.
```SQL
SELECT * FROM Students, Courses;
```
