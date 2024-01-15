# Lab 04

## 1. given

```sql
CREATE DATABASE The_Office;

CREATE TABLE Employee (
    Emp_ID char(4),
    Name varchar(50),
    Age int,
    Role varchar(30),
    Salary int,
    Joining_Date date
);
```

## 2. given

```sql
INSERT INTO Employee VALUES
("E001", "Michael Scott`, 40, "Manager", 100000, "1999-09-20"),
( "E002", "Jim Harper", 30, "Sales Executive", 60000, "2004-09-30"),
("E003", "Pam Beesly", 28, "Receptionist", 25000, "2003-09-30" ),
("E004", "Angela Martin", 33, "Accountant", 65000, "2005-09-28" ),
("E005", "Dwight Shrute", 32, "Assistant Manager", 60000, "2003-09-30" ),
("E006", "Kelly Kapoor", 29, "Marketing Executive", 45000, "2003-09-30" ),
("E007", "Andrew Bernard", 30, "Sales Executive", 50000, "2007-05-10" ),
("E008", "Kevin Malone", 28, "Accountant", 60000, "2004-10-30" ),
("E009", "Toby Flender", 35, "HR Manager", 70000, "2004-09-30" ),
("E010", "Phyllis Vance", 40, "Sales Executive", 61000, "1999-09-20" ),
("E011", "Creed Bratton", 50, "Sales Executive", 80000, "1980-06-01");
```

## 3. Complete all tasks below:

- [ ] Find the name and role of employees whose name starts with `a` or ends with `e`
- [ ] Find the details of Employees who have salary between 40000 and 60000
- [ ] Find the details of employees who have joined before the year 2000.
- [ ] There will be 5% raise in salary for all sales executives, as they have done an excellent job last year. Update the table with the new raised salary. Check if the salary was updated.
- [ ] Michael Scott will get a bonus of 20% on his salary for excellent leadership initiatives in last year. Calculate his bonus and use alias (`Michael_Bonus`) for the column header. [Note: You should not update his salary. Only show the bonus]
- [ ] Show the details of all employees according to their salary sorted from higher to lower.
- [ ] Show the details of all employees according to their age sorted from lower to higher.
- [ ] Show details of employees whose age is more than 35 and who joined before 2003.
- [ ] Turns out Creed Bratton has been lying about his age, he is actually 80 years old. So he should retire. Delete him from the table.
- [ ] Find the details of employees who have the word `executive` in their role.
- [ ] Change the attribute `Name` to `Employee_Name`
- [ ] Add attribute `Bonus` to the employee table.
- [ ] Delete attribute `Bonus` from the table.
- [ ] List the names of different job roles in the office. There should not be any repetition in your list.
