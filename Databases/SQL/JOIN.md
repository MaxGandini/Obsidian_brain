An example in pure SQL for the employees and departments tables:

```SQL
SELECT employees.name, departments.name AS department_name
FROM employees
JOIN departments ON employees.department_id = departments.id;
```
