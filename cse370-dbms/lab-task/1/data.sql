-- 1
-- table query
CREATE TABLE
  `Developers` (
    member_id INTEGER,
    name VARCHAR(59),
    email VARCHAR(59),
    influence_count INTEGER,
    Joining_date DATE,
    multiplier INTEGER
  );

-- inserting all data
INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    1,
    'Taylor Otwell',
    'otwell@laravel.com',
    739360,
    '2020-6-10',
    10
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    2,
    'Ryan Dahl',
    'ryan@nodejs.org',
    633632,
    '2020-04-22',
    10
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    3,
    'Brendan Eich',
    'eich@javascript.com',
    939570,
    '2020-05-07',
    8
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    5,
    'Evan You',
    'you@vuejs.org',
    982630,
    '2020-06-11',
    7
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    6,
    'Rasmus Lerdorf',
    'lerdorf@php.net',
    937927,
    '2020-06-3',
    8
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    7,
    'Guido van Rossum',
    'guido@python.org',
    968827,
    '2020-07-18',
    19
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    8,
    'Adrian Holovaty',
    'adrian@djangoproject.com',
    570724,
    '2020-05-07',
    5
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    9,
    'Simon Willison',
    'simon@djangoproject.com',
    864615,
    '2020-04-30',
    4
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    10,
    'James Gosling',
    'james@java.com',
    719491,
    '2020-05-18',
    5
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    11,
    'Rod Johnson',
    'rod@spring.io',
    601744,
    '2020-05-18',
    7
  );

INSERT INTO
  Developers (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    12,
    'Satoshi Nakamoto',
    'nakamoto@blockchain.com',
    630488,
    '2020-05-10',
    10
  );

-- oneliner
INSERT INTO
  `Developers` (
    member_id,
    name,
    email,
    influence_count,
    Joining_date,
    multiplier
  )
VALUES
  (
    1,
    'Taylor Otwell',
    'otwell@laravel.com',
    739360,
    '2020-6-10',
    10
  ),
  (
    2,
    'Ryan Dahl',
    'ryan@nodejs.org',
    633632,
    '2020-04-22',
    10
  ),
  (
    3,
    'Brendan Eich',
    'eich@javascript.com',
    939570,
    '2020-05-07',
    8
  ),
  (
    5,
    'Evan You',
    'you@vuejs.org',
    982630,
    '2020-06-11',
    7
  ),
  (
    6,
    'Rasmus Lerdorf',
    'lerdorf@php.net',
    937927,
    '2020-06-3',
    8
  ),
  (
    7,
    'Guido van Rossum',
    'guido@python.org',
    968827,
    '2020-07-18',
    19
  ),
  (
    8,
    'Adrian Holovaty',
    'adrian@djangoproject.com',
    570724,
    '2020-05-07',
    5
  ),
  (
    9,
    'Simon Willison',
    'simon@djangoproject.com',
    864615,
    '2020-04-30',
    4
  ),
  (
    10,
    'James Gosling',
    'james@java.com',
    719491,
    '2020-05-18',
    5
  ),
  (
    11,
    'Rod Johnson',
    'rod@spring.io',
    601744,
    '2020-05-18',
    7
  ),
  (
    12,
    'Satoshi Nakamoto',
    'nakamoto@blockchain.com',
    630488,
    '2020-05-10',
    10
  );

-- 2
ALTER TABLE `Developers` CHANGE COLUMN `influence_count` -- old name; notice optional backticks
`followers` -- new name
INTEGER;

-- must include all the datatype info
-- raw
ALTER TABLE `Developers` CHANGE COLUMN `influence_count` `followers` INTEGER;

ALTER TABLE `Developers` CHANGE COLUMN `followers` `influence_count` INTEGER;

-- 3
UPDATE `Developers`
SET
  followers = followers + 10;

--  4
SELECT
  name,
  email,
  followers
from
  Developers;

-- 5
ALTER TABLE `Developers` CHANGE COLUMN `multiplier` `multipliers` INTEGER;

SELECT
  name,
  (
    (followers * 100 / 1000000) * (multipliers * 100 / 20)
  ) / 100 AS Efficiency
FROM
  `Developers`;
