-- 1: Done
-- Find the first_name, last_name, email, phone_number, hire_date and department_id of all the employees with the latest hire_date.
SELECT
  first_name,
  last_name,
  email,
  phone_number,
  hire_date,
  department_id
FROM
  `employees`
where
  hire_date = (
    Select
      max(hire_date)
    from
      employees
  );

-- 2: Done
-- Find the first_name, last_name, employee_id, phone_number, salary and department_id of all the employees with the lowest salary in each department. 
Select
  first_name,
  last_name,
  employee_id,
  phone_number,
  salary,
  department_id
from
  employees
where
  (department_id, salary) in (
    Select
      department_id,
      MIN(salary)
    from
      employees
    group by
      department_id
  )
ORDER by
  department_id;

-- 3: Done
-- Find the first_name, last_name, employee_id, commission_pct and department_id of all the employees in department XYZABC (department_id = 7) who have a lower commission_pct than all of the employees of department ABCXYZ(department_id = 5).
Select
  first_name,
  last_name,
  employee_id,
  commission_pct,
  department_id
from
  employees
where
  department_id = 7
  and commission_pct < (
    Select
      MIN(commission_pct)
    from
      employees
    where
      department_id = 5
  );

-- 4: done
-- Find the department_id and total number of employees of each department which does not have a single employee under it with a salary more than 30,000.
SELECT
  department_id,
  COUNT(*) as Total_Count
FROM
  employees
GROUP BY
  department_id
having
  MAX(salary) <= 30000;

-- 5: done
-- For each of the departments, find the department_id, job_id and commission_pct with commission_pct less than at least one other job_id in that department.
SELECT
  department_id,
  job_id,
  commission_pct
from
  employees
where
  commission_pct < any (
    Select
      MAX(commission_pct)
    from
      employees
    group BY
      department_id
  )
ORDER BY
  commission_pct;

-- 6: done
-- Find the manager_id who does not have any employee under them with a salary less than 3500.
SELECT
  manager_id
FROM
  employees
GROUP BY
  manager_id
having
  MIN(salary) >= 3500;

-- 7 ?
-- Find the first_name, last_name, employee_id, email, salary, department_id and commission_pct of the employee who has the lowest commission_pct under each manager.
Select
  first_name,
  last_name,
  employee_id,
  email,
  salary,
  department_id,
  commission_pct
from
  employees
where
  (manager_id, commission_pct) in (
    Select
      manager_id,
      MIN(commission_pct)
    from
      employees
    group by
      manager_id
  )
ORDER by
  department_id;
