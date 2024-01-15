CREATE TABLE
  employees (
    employee_id char(10),
    first_name varchar(20),
    last_name varchar(20),
    email varchar(60),
    phone_number char(14),
    hire_date date,
    job_id int,
    salary int,
    commission_pct decimal(5, 3),
    manager_id char(10),
    department_id int
  );

UPDATE employees
SET
  department_id = 7
WHERE
  department_id = 3;
