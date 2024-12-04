See [[SQL]] For the context .

```SQL
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 70000;  -- Show only departments with avg salary > 70K
```
