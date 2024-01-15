-- (1)
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
ORDER by
  hire_date DESC;
