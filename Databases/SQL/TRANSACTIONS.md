```SQL
BEGIN;

INSERT INTO employees (name, department, salary, hire_date)
VALUES ('Charlie', 'Finance', 75000.00, '2023-03-01');

UPDATE employees
SET salary = salary + 5000
WHERE name = 'Alice';

COMMIT;  -- Save changes
-- ROLLBACK;  -- Undo changes if needed
```
