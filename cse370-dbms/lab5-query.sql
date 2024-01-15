 -- task 1
create table
  customer (
    customer_id varchar(10) not null,
    customer_name varchar(20) not null,
    customer_street varchar(30),
    customer_city varchar(30),
    primary key (customer_id)
  );

create table
  branch (
    branch_name varchar(15),
    branch_city varchar(30),
    assets int,
    primary key (branch_name),
    check (assets >= 0)
  );

create table
  account (
    branch_name varchar(15),
    account_number varchar(10) not null,
    balance int,
    primary key (account_number),
    check (balance >= 0)
  );

create table
  loan (
    loan_number varchar(10) not null,
    branch_name varchar(15),
    amount int,
    primary key (loan_number)
  );

create table
  depositor (
    customer_id varchar(10) not null,
    account_number varchar(10) not null,
    primary key (customer_id, account_number),
    foreign key (customer_id) references customer (customer_id),
    foreign key (account_number) references account (account_number)
  );

create table
  borrower (
    customer_id varchar(10) not null,
    loan_number varchar(10) not null,
    primary key (customer_id, loan_number),
    foreign key (customer_id) references customer (customer_id),
    foreign key (loan_number) references loan (loan_number)
  );

-- task 2
insert into
  customer
values
  ('C-101', 'Jones', 'Main', 'Harrison'),
  ('C-201', 'Smith', 'North', 'Rye'),
  ('C-211', 'Hayes', 'Main', 'Harrison'),
  ('C-212', 'Curry', 'North', 'Rye'),
  ('C-215', 'Lindsay', 'Park', 'Pittsfield'),
  ('C-220', 'Turner', 'Putnam', 'Stamford'),
  ('C-222', 'Williams', 'Nassau', 'Princeton'),
  ('C-225', 'Adams', 'Spring', 'Pittsfield'),
  ('C-226', 'Johnson', 'Alma', 'Palo Alto'),
  ('C-233', 'Glenn', 'Sand Hill', 'Woodside'),
  ('C-234', 'Brooks', 'Senator', 'Brooklyn'),
  ('C-255', 'Green', 'Walnut', 'Stamford');

insert into
  branch
values
  ('Downtown', 'Brooklyn', 9000000),
  ('Redwood', 'Palo Alto', 2100000),
  ('Perryridge', 'Horseneck', 1700000),
  ('Mianus', 'Horseneck', 400000),
  ('Round Hill', 'Horseneck', 8000000),
  ('Pownal', 'Bennington', 300000),
  ('North Town', 'Rye', 3700000),
  ('Brighton', 'Brooklyn', 7100000);

insert into
  account
values
  ('Downtown', 'A-101', 500),
  ('Mianus', 'A-215', 700),
  ('Perryridge', 'A-102', 400),
  ('Round Hill', 'A-
305', 350),
  ('Brighton', 'A-201', 900),
  ('Redwood', 'A-222', 700),
  ('Brighton', 'A-217', 750);

insert into
  loan
values
  ('L-17', 'Downtown', 1000),
  ('L-23', 'Redwood', 2000),
  ('L-15', 'Perryridge', 1500),
  ('L-14', 'Downtown', 1500),
  ('L-93', 'Mianus', 500),
  ('L-11', 'Round Hill', 900),
  ('L-16', 'Perryridge', 1300);

insert into
  depositor
values
  ('C-226', 'A-101'),
  ('C-201', 'A-215'),
  ('C-211', 'A-102'),
  ('C-220', 'A-305'),
  ('C-226', 'A-201'),
  ('C-
101', 'A-217'),
  ('C-215', 'A-222');

insert into
  borrower
values
  ('C-101', 'L-17'),
  ('C-201', 'L-23'),
  ('C-211', 'L-15'),
  ('C-226', 'L-14'),
  ('C-212', 'L-93'),
  ('C-201', 'L-11'),
  ('C-222', 'L-17'),
  ('C-225', 'L-16');

-- task3
-- general format
-- Select * from Table1 inner join Table2 on Table1.attribute=Table2.attribute;
-- task4
-- General format
-- Select
--   *
-- from
--   (
--     (
--       Table1
--       inner join Table2 on Table1.attribute = Table2.attribute
--     )
--     inner join Table 3 on Table3.attribute = Table1 / 2.attribute
--   );
-- task5
-- Select * from T1, T2, T3,…..Tn where T1.attr=T2.attr […..other conditions] ;
-- task6
-- task7
-- task8
