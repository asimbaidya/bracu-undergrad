-- (1)
-- Show all the unique dates of the users joining in ascending order. [1]
select distinct
  joining_date
from
  Developers
order by
  joining_date asc;

-- final
SELECT DISTINCT
  `joining_date` as `Joined`
FROM
  `Developers`
ORDER BY
  `joining_date` ASC;

-- (2)
-- show the name and email of the Developers who have the 5 highest numbers of followers. [2]
select
  name,
  email
from
  Developers
order by
  followers desc
limit
  5;

-- final
SELECT
  `name`,
  `email`
FROM
  `Developers`
ORDER BY
  `followers` DESC
LIMIT
  50;

-- (3)
-- count the number of Developers in each multiplier [2]
select
  `multipliers`,
  count(*) as `Number of Developer`
from
  `Developers`
group by
  `multipliers`;

-- final
SELECT
  `multipliers`,
  COUNT(*) AS `Number of Developer`
FROM
  `Developers`
GROUP BY
  `multipliers`;

-- (4) (buggy)
-- Show the name of the user with the maximum multiplier among the developers whose number of followers is less than 700000. [2]
SELECT
  name,
  followers,
  multipliers
FROM
  Developers
WHERE
  followers < 700000
ORDER BY
  multipliers DESC,
  followers ASC;

-- final
SELECT
  `name`,
  `followers`,
  `multipliers`
FROM
  `Developers`
WHERE
  `followers` < 700000
ORDER BY
  `multipliers` DESC,
  `followers` ASC;

-- (5)
-- Find the average of the number of followers but only consider the members who joined before 11 June 2020. [2]
SELECT
  AVG(followers) as `average_followers of users who joined before 2020-06-11`
from
  Developers
WHERE
  Joining_date < '2020-06-11';

-- final
SELECT
  AVG(`followers`) AS `average_followers of users who joined before 2020-06-11`
FROM
  `Developers`
WHERE
  `Joining_date` < '2020-06-11';

-- (6)
-- Retrieve the id, name, email, and followers of the Developers who have either “.com” or “.net” in their email address. [1]
SELECT
  member_id as id,
  name,
  email,
  followers
FROM
  Developers
WHERE
  email LIKE '%.com'
  OR email LIKE '%.net';

-- final
SELECT
  `member_id` AS `Developer ID`,
  `name`,
  `email`,
  `followers`
FROM
  `Developers`
WHERE
  `email` LIKE '%.com'
  OR `email` LIKE '%.net';
