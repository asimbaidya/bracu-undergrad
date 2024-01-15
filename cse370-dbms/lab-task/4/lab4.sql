-- | account          |
-- | borrower         |
-- | branch           |
-- | customer         |
-- | depositor        |
-- | loan
-- (1)
SELECT
  customer.customer_name as name,
  loan.loan_number
from
  (
    (
      customer
      INNER JOIN borrower on customer.customer_id = borrower.customer_id
    )
    INNER JOIN loan on borrower.loan_number = loan.loan_number
  )
WHERE
  branch_name = "DownTown";

-- (2)
SELECT
  C1.customer_name AS Customer1,
  C2.customer_name AS Customer2,
  C1.customer_city AS City
FROM
  customer C1
  JOIN customer C2 ON C1.customer_name < C2.customer_name
  AND C1.customer_city = C2.customer_city;

-- (3)
SELECT
  `branch_name` AS `Branch_name`,
  SUM((balance * 4) / 100) AS `Total_interest`
FROM
  `account`
GROUP BY
  `branch_name`;

-- (4)
SELECT
  D.account_number AS Account_number,
  MAX(A.balance) AS Highest_balance,
  C.customer_city AS City
FROM
  (
    customer C
    INNER JOIN depositor D on C.customer_id = D.customer_id
  )
  inner join account A on D.account_number = A.account_number
GROUP BY
  C.customer_city;

-- (5)
SELECT
  *
FROM
  (
    SELECT
      L.loan_number,
      L.amount AS loan_amount,
      C.customer_name
    FROM
      (
        borrower B
        INNER JOIN loan L ON L.loan_number = B.loan_number
      )
      INNER JOIN customer C ON B.customer_id = C.customer_id
    ORDER BY
      L.amount DESC
    LIMIT
      5
  ) AS L
ORDER BY
  loan_amount ASC,
  loan_number DESC;

-- (6)
SELECT
  C.customer_name
FROM
  (
    (
      loan L
      INNER JOIN account A ON L.branch_name = A.branch_name
    )
    INNER JOIN borrower B ON L.loan_number = B.loan_number
  )
  INNER JOIN customer C ON B.customer_id = C.customer_id
WHERE
  A.branch_name = "Perryridge"
  and L.branch_name = "Perryridge"
GROUP BY
  A.branch_name;

-- (7)
SELECT
  C.customer_name,
  SUM(L.amount) AS total_loan
FROM
  (
    loan L
    INNER JOIN borrower B on L.loan_number = B.loan_number
  )
  INNER JOIN customer C ON B.customer_id = C.customer_id
GROUP BY
  C.customer_id
HAVING
  count(*) >= 2;
