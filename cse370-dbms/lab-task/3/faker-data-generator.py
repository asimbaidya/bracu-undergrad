from random import choice

from faker import Faker

fake = Faker()
# Faker.seed(4321)
Faker.seed(93)


MAIL_SERVERS = ["gmail"]
# emp_id -> uniq
PHN_NUMS = ["01323432423", "0132342343", "01334343"]
HIRE_DATE = []  # done
# JOB_ID = [] # uniq
SALARY = []  # done
C_PCT = [
    0.2,
    0.3,
    0.5,
    0.6,
    0.7,
]
MANAGER_ID = ["X1", "X2", "X3", "X4", "X5"]
DEPT_ID = [1, 3, 4, 5, 7, 8]

for _ in range(20):
    HIRE_DATE.append(fake.date())
for m in range(1, 30):
    SALARY.append(m * 3000)


print(
    """CREATE TABLE employees (
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


INSERT INTO employees(
    employee_id,
    first_name,
    last_name,
    email,
    phone_number,
    hire_date,
    job_id,
    salary,
    commission_pct,
    manager_id,
    department_id
) VALUES
"""
)

# data creation
for i in range(1, 101):
    e_id = f"{i}"
    fn, ln = fake.first_name(), fake.last_name()
    email = f"{fn.lower()}.{ln.lower()}@{choice(MAIL_SERVERS)}.com"
    phn = choice(PHN_NUMS)
    hire_date = choice(HIRE_DATE)
    job_id = i * 200
    salary = choice(SALARY)
    c_pct = choice(C_PCT)
    m_id = choice(MANAGER_ID)
    # d_id = choice(DEPT_ID)
    d_id = 7

    if i != 100:
        print(
            f"('{e_id}', '{fn}', '{ln}', '{email}', '{phn}', '{hire_date}', {job_id}, {salary}, {c_pct}, '{m_id}', {d_id}),"
        )
    else:
        print(
            f"('{e_id}', '{fn}', '{ln}', '{email}', '{phn}', '{hire_date}', {job_id}, {salary}, {c_pct}, '{m_id}', {d_id});"
        )
