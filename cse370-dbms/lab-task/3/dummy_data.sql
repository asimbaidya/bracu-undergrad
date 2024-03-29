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

INSERT INTO
  employees (
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
  )
VALUES
  (
    '1',
    'Raymond',
    'Martinez',
    'raymond.martinez@gmail.com',
    '01323432423',
    '1981-10-06',
    200,
    21000,
    0.5,
    'X5',
    7
  ),
  (
    '2',
    'Chad',
    'Boyle',
    'chad.boyle@gmail.com',
    '01323432423',
    '2003-08-23',
    400,
    87000,
    0.2,
    'X1',
    7
  ),
  (
    '3',
    'Jamie',
    'Walker',
    'jamie.walker@gmail.com',
    '01334343',
    '2012-03-12',
    600,
    69000,
    0.6,
    'X4',
    7
  ),
  (
    '4',
    'Diana',
    'Olson',
    'diana.olson@gmail.com',
    '01334343',
    '1972-03-30',
    800,
    54000,
    0.2,
    'X3',
    7
  ),
  (
    '5',
    'Brittany',
    'Wheeler',
    'brittany.wheeler@gmail.com',
    '01334343',
    '1976-03-31',
    1000,
    69000,
    0.7,
    'X1',
    7
  ),
  (
    '6',
    'Matthew',
    'Barry',
    'matthew.barry@gmail.com',
    '0132342343',
    '1976-03-31',
    1200,
    9000,
    0.2,
    'X5',
    7
  ),
  (
    '7',
    'Thomas',
    'Brown',
    'thomas.brown@gmail.com',
    '01334343',
    '2003-08-23',
    1400,
    84000,
    0.3,
    'X2',
    7
  ),
  (
    '8',
    'Brian',
    'Greene',
    'brian.greene@gmail.com',
    '0132342343',
    '1972-03-30',
    1600,
    18000,
    0.7,
    'X5',
    7
  ),
  (
    '9',
    'Karen',
    'Costa',
    'karen.costa@gmail.com',
    '01334343',
    '1978-02-07',
    1800,
    21000,
    0.3,
    'X2',
    7
  ),
  (
    '10',
    'Christopher',
    'Avila',
    'christopher.avila@gmail.com',
    '0132342343',
    '2012-04-22',
    2000,
    87000,
    0.3,
    'X2',
    7
  ),
  (
    '11',
    'Lisa',
    'Harris',
    'lisa.harris@gmail.com',
    '01323432423',
    '1980-12-17',
    2200,
    66000,
    0.7,
    'X3',
    7
  ),
  (
    '12',
    'Kimberly',
    'Hart',
    'kimberly.hart@gmail.com',
    '01323432423',
    '1977-09-24',
    2400,
    27000,
    0.7,
    'X3',
    7
  ),
  (
    '13',
    'Eric',
    'Alexander',
    'eric.alexander@gmail.com',
    '01323432423',
    '2007-08-30',
    2600,
    81000,
    0.6,
    'X3',
    7
  ),
  (
    '14',
    'Pamela',
    'Paul',
    'pamela.paul@gmail.com',
    '01334343',
    '2007-08-30',
    2800,
    33000,
    0.3,
    'X5',
    7
  ),
  (
    '15',
    'Christopher',
    'Long',
    'christopher.long@gmail.com',
    '01334343',
    '2012-04-22',
    3000,
    66000,
    0.6,
    'X1',
    7
  ),
  (
    '16',
    'Franklin',
    'Holt',
    'franklin.holt@gmail.com',
    '0132342343',
    '1994-03-09',
    3200,
    15000,
    0.7,
    'X2',
    7
  ),
  (
    '17',
    'Douglas',
    'Medina',
    'douglas.medina@gmail.com',
    '01334343',
    '1994-01-16',
    3400,
    42000,
    0.5,
    'X2',
    7
  ),
  (
    '18',
    'Christopher',
    'Swanson',
    'christopher.swanson@gmail.com',
    '01334343',
    '2019-03-14',
    3600,
    36000,
    0.2,
    'X4',
    7
  ),
  (
    '19',
    'Jean',
    'Decker',
    'jean.decker@gmail.com',
    '01334343',
    '2008-07-03',
    3800,
    33000,
    0.6,
    'X4',
    7
  ),
  (
    '20',
    'Michael',
    'Miller',
    'michael.miller@gmail.com',
    '01334343',
    '2012-03-12',
    4000,
    12000,
    0.3,
    'X1',
    7
  ),
  (
    '21',
    'Aaron',
    'Pierce',
    'aaron.pierce@gmail.com',
    '01334343',
    '2003-08-23',
    4200,
    66000,
    0.3,
    'X4',
    7
  ),
  (
    '22',
    'Anthony',
    'Shaw',
    'anthony.shaw@gmail.com',
    '01334343',
    '1976-03-31',
    4400,
    69000,
    0.2,
    'X4',
    7
  ),
  (
    '23',
    'Andrew',
    'Mcdaniel',
    'andrew.mcdaniel@gmail.com',
    '0132342343',
    '2016-03-10',
    4600,
    51000,
    0.5,
    'X1',
    7
  ),
  (
    '24',
    'Sharon',
    'Smith',
    'sharon.smith@gmail.com',
    '01334343',
    '1994-03-09',
    4800,
    42000,
    0.6,
    'X1',
    7
  ),
  (
    '25',
    'William',
    'Randolph',
    'william.randolph@gmail.com',
    '01334343',
    '1994-01-16',
    5000,
    84000,
    0.7,
    'X4',
    7
  ),
  (
    '26',
    'Veronica',
    'Camacho',
    'veronica.camacho@gmail.com',
    '0132342343',
    '2019-03-14',
    5200,
    66000,
    0.6,
    'X5',
    7
  ),
  (
    '27',
    'William',
    'Mathis',
    'william.mathis@gmail.com',
    '01323432423',
    '1978-02-07',
    5400,
    27000,
    0.2,
    'X1',
    7
  ),
  (
    '28',
    'Maria',
    'Kirby',
    'maria.kirby@gmail.com',
    '01334343',
    '2008-07-03',
    5600,
    69000,
    0.2,
    'X3',
    7
  ),
  (
    '29',
    'Susan',
    'Adams',
    'susan.adams@gmail.com',
    '0132342343',
    '1994-03-09',
    5800,
    30000,
    0.6,
    'X3',
    7
  ),
  (
    '30',
    'Jeffrey',
    'Bell',
    'jeffrey.bell@gmail.com',
    '01334343',
    '1978-02-07',
    6000,
    78000,
    0.2,
    'X5',
    7
  ),
  (
    '31',
    'Evan',
    'Sandoval',
    'evan.sandoval@gmail.com',
    '01323432423',
    '1994-01-16',
    6200,
    33000,
    0.2,
    'X4',
    7
  ),
  (
    '32',
    'Frances',
    'Stewart',
    'frances.stewart@gmail.com',
    '01334343',
    '1994-01-16',
    6400,
    51000,
    0.6,
    'X5',
    7
  ),
  (
    '33',
    'Timothy',
    'Medina',
    'timothy.medina@gmail.com',
    '0132342343',
    '1972-03-30',
    6600,
    87000,
    0.2,
    'X2',
    7
  ),
  (
    '34',
    'Brenda',
    'Hale',
    'brenda.hale@gmail.com',
    '01323432423',
    '1994-01-16',
    6800,
    15000,
    0.7,
    'X2',
    7
  ),
  (
    '35',
    'Grant',
    'Mcconnell',
    'grant.mcconnell@gmail.com',
    '01323432423',
    '1980-12-17',
    7000,
    66000,
    0.7,
    'X4',
    7
  ),
  (
    '36',
    'Bethany',
    'Powell',
    'bethany.powell@gmail.com',
    '01334343',
    '1994-01-16',
    7200,
    63000,
    0.5,
    'X3',
    7
  ),
  (
    '37',
    'Dominic',
    'Nelson',
    'dominic.nelson@gmail.com',
    '0132342343',
    '1972-03-30',
    7400,
    66000,
    0.6,
    'X4',
    7
  ),
  (
    '38',
    'Miranda',
    'Bennett',
    'miranda.bennett@gmail.com',
    '01334343',
    '1977-09-24',
    7600,
    3000,
    0.5,
    'X5',
    7
  ),
  (
    '39',
    'Melissa',
    'Martin',
    'melissa.martin@gmail.com',
    '01334343',
    '2008-07-03',
    7800,
    3000,
    0.3,
    'X1',
    7
  ),
  (
    '40',
    'Karen',
    'Richardson',
    'karen.richardson@gmail.com',
    '01323432423',
    '1994-03-09',
    8000,
    39000,
    0.3,
    'X1',
    7
  ),
  (
    '41',
    'Anthony',
    'Hunter',
    'anthony.hunter@gmail.com',
    '0132342343',
    '2003-08-23',
    8200,
    24000,
    0.3,
    'X4',
    7
  ),
  (
    '42',
    'Ashley',
    'Johnson',
    'ashley.johnson@gmail.com',
    '01323432423',
    '1994-01-16',
    8400,
    54000,
    0.6,
    'X4',
    7
  ),
  (
    '43',
    'Deanna',
    'Lucas',
    'deanna.lucas@gmail.com',
    '0132342343',
    '1996-08-20',
    8600,
    60000,
    0.6,
    'X4',
    7
  ),
  (
    '44',
    'Brooke',
    'Miller',
    'brooke.miller@gmail.com',
    '01334343',
    '1996-08-20',
    8800,
    54000,
    0.6,
    'X2',
    7
  ),
  (
    '45',
    'Craig',
    'Medina',
    'craig.medina@gmail.com',
    '0132342343',
    '1978-04-18',
    9000,
    30000,
    0.5,
    'X4',
    7
  ),
  (
    '46',
    'Rebecca',
    'Martinez',
    'rebecca.martinez@gmail.com',
    '0132342343',
    '2009-08-01',
    9200,
    75000,
    0.6,
    'X4',
    7
  ),
  (
    '47',
    'Janice',
    'Ryan',
    'janice.ryan@gmail.com',
    '01323432423',
    '2008-07-03',
    9400,
    81000,
    0.5,
    'X1',
    7
  ),
  (
    '48',
    'Christian',
    'Henson',
    'christian.henson@gmail.com',
    '01323432423',
    '1996-08-20',
    9600,
    51000,
    0.7,
    'X2',
    7
  ),
  (
    '49',
    'Sheri',
    'Patterson',
    'sheri.patterson@gmail.com',
    '01323432423',
    '1977-09-24',
    9800,
    27000,
    0.5,
    'X2',
    7
  ),
  (
    '50',
    'James',
    'Oliver',
    'james.oliver@gmail.com',
    '01323432423',
    '2008-07-03',
    10000,
    12000,
    0.6,
    'X4',
    7
  ),
  (
    '51',
    'Tiffany',
    'Knox',
    'tiffany.knox@gmail.com',
    '0132342343',
    '1976-03-31',
    10200,
    18000,
    0.7,
    'X4',
    7
  ),
  (
    '52',
    'Jennifer',
    'Rose',
    'jennifer.rose@gmail.com',
    '01334343',
    '1978-02-07',
    10400,
    36000,
    0.7,
    'X5',
    7
  ),
  (
    '53',
    'Jeremiah',
    'Williams',
    'jeremiah.williams@gmail.com',
    '01323432423',
    '2009-08-01',
    10600,
    39000,
    0.6,
    'X4',
    7
  ),
  (
    '54',
    'Mariah',
    'Escobar',
    'mariah.escobar@gmail.com',
    '0132342343',
    '1995-01-13',
    10800,
    24000,
    0.6,
    'X4',
    7
  ),
  (
    '55',
    'Kevin',
    'Price',
    'kevin.price@gmail.com',
    '01334343',
    '1978-02-07',
    11000,
    45000,
    0.2,
    'X5',
    7
  ),
  (
    '56',
    'Jacob',
    'Alexander',
    'jacob.alexander@gmail.com',
    '01323432423',
    '2019-03-14',
    11200,
    21000,
    0.7,
    'X4',
    7
  ),
  (
    '57',
    'Kristen',
    'Jones',
    'kristen.jones@gmail.com',
    '0132342343',
    '2003-08-23',
    11400,
    39000,
    0.3,
    'X1',
    7
  ),
  (
    '58',
    'Mary',
    'Brown',
    'mary.brown@gmail.com',
    '01323432423',
    '1976-03-31',
    11600,
    84000,
    0.5,
    'X5',
    7
  ),
  (
    '59',
    'Russell',
    'Austin',
    'russell.austin@gmail.com',
    '01334343',
    '1996-08-20',
    11800,
    42000,
    0.7,
    'X3',
    7
  ),
  (
    '60',
    'Danielle',
    'Bentley',
    'danielle.bentley@gmail.com',
    '01323432423',
    '2012-04-22',
    12000,
    27000,
    0.7,
    'X2',
    7
  ),
  (
    '61',
    'David',
    'Garcia',
    'david.garcia@gmail.com',
    '01334343',
    '1972-03-30',
    12200,
    3000,
    0.6,
    'X4',
    7
  ),
  (
    '62',
    'James',
    'Nguyen',
    'james.nguyen@gmail.com',
    '01323432423',
    '1980-12-17',
    12400,
    15000,
    0.3,
    'X2',
    7
  ),
  (
    '63',
    'Julia',
    'Gonzalez',
    'julia.gonzalez@gmail.com',
    '01334343',
    '2009-08-01',
    12600,
    60000,
    0.6,
    'X3',
    7
  ),
  (
    '64',
    'Logan',
    'Green',
    'logan.green@gmail.com',
    '01334343',
    '2019-03-14',
    12800,
    87000,
    0.5,
    'X2',
    7
  ),
  (
    '65',
    'Lance',
    'Stone',
    'lance.stone@gmail.com',
    '01323432423',
    '2003-08-23',
    13000,
    69000,
    0.6,
    'X2',
    7
  ),
  (
    '66',
    'Alisha',
    'Graham',
    'alisha.graham@gmail.com',
    '0132342343',
    '2003-08-23',
    13200,
    75000,
    0.5,
    'X1',
    7
  ),
  (
    '67',
    'Hunter',
    'Terrell',
    'hunter.terrell@gmail.com',
    '01323432423',
    '2012-04-22',
    13400,
    57000,
    0.7,
    'X5',
    7
  ),
  (
    '68',
    'Michael',
    'White',
    'michael.white@gmail.com',
    '01334343',
    '2008-07-03',
    13600,
    36000,
    0.2,
    'X3',
    7
  ),
  (
    '69',
    'Brett',
    'Cohen',
    'brett.cohen@gmail.com',
    '01334343',
    '1976-03-31',
    13800,
    9000,
    0.3,
    'X3',
    7
  ),
  (
    '70',
    'Destiny',
    'Miller',
    'destiny.miller@gmail.com',
    '0132342343',
    '2019-03-14',
    14000,
    6000,
    0.5,
    'X2',
    7
  ),
  (
    '71',
    'John',
    'Robles',
    'john.robles@gmail.com',
    '0132342343',
    '2003-08-23',
    14200,
    27000,
    0.5,
    'X4',
    7
  ),
  (
    '72',
    'Charlene',
    'Short',
    'charlene.short@gmail.com',
    '01323432423',
    '2007-08-30',
    14400,
    81000,
    0.3,
    'X1',
    7
  ),
  (
    '73',
    'Debra',
    'Ramirez',
    'debra.ramirez@gmail.com',
    '01323432423',
    '1994-03-09',
    14600,
    66000,
    0.6,
    'X5',
    7
  ),
  (
    '74',
    'Heather',
    'Duncan',
    'heather.duncan@gmail.com',
    '01334343',
    '2003-08-23',
    14800,
    54000,
    0.5,
    'X1',
    7
  ),
  (
    '75',
    'Tina',
    'Rios',
    'tina.rios@gmail.com',
    '01323432423',
    '1976-03-31',
    15000,
    87000,
    0.2,
    'X1',
    7
  ),
  (
    '76',
    'Juan',
    'Murillo',
    'juan.murillo@gmail.com',
    '01323432423',
    '2012-04-22',
    15200,
    18000,
    0.7,
    'X5',
    7
  ),
  (
    '77',
    'Rebecca',
    'Fowler',
    'rebecca.fowler@gmail.com',
    '0132342343',
    '1994-01-16',
    15400,
    24000,
    0.7,
    'X2',
    7
  ),
  (
    '78',
    'Alexis',
    'Boyer',
    'alexis.boyer@gmail.com',
    '0132342343',
    '1977-09-24',
    15600,
    72000,
    0.2,
    'X4',
    7
  ),
  (
    '79',
    'Hannah',
    'Rose',
    'hannah.rose@gmail.com',
    '01334343',
    '2012-03-12',
    15800,
    63000,
    0.5,
    'X1',
    7
  ),
  (
    '80',
    'David',
    'Garcia',
    'david.garcia@gmail.com',
    '01323432423',
    '1994-01-16',
    16000,
    81000,
    0.7,
    'X3',
    7
  ),
  (
    '81',
    'Diana',
    'Stanley',
    'diana.stanley@gmail.com',
    '0132342343',
    '1976-03-31',
    16200,
    72000,
    0.2,
    'X3',
    7
  ),
  (
    '82',
    'Mary',
    'Sparks',
    'mary.sparks@gmail.com',
    '01334343',
    '1978-04-18',
    16400,
    30000,
    0.5,
    'X2',
    7
  ),
  (
    '83',
    'Amy',
    'Drake',
    'amy.drake@gmail.com',
    '01334343',
    '1996-08-20',
    16600,
    66000,
    0.7,
    'X1',
    7
  ),
  (
    '84',
    'Stephanie',
    'Anderson',
    'stephanie.anderson@gmail.com',
    '01334343',
    '2012-03-12',
    16800,
    45000,
    0.6,
    'X1',
    7
  ),
  (
    '85',
    'Jacob',
    'Wright',
    'jacob.wright@gmail.com',
    '01323432423',
    '1981-10-06',
    17000,
    78000,
    0.3,
    'X2',
    7
  ),
  (
    '86',
    'Barry',
    'Banks',
    'barry.banks@gmail.com',
    '0132342343',
    '2016-03-10',
    17200,
    84000,
    0.5,
    'X3',
    7
  ),
  (
    '87',
    'David',
    'Duncan',
    'david.duncan@gmail.com',
    '01323432423',
    '2016-03-10',
    17400,
    54000,
    0.3,
    'X4',
    7
  ),
  (
    '88',
    'Andrew',
    'Roberts',
    'andrew.roberts@gmail.com',
    '0132342343',
    '2008-07-03',
    17600,
    87000,
    0.3,
    'X4',
    7
  ),
  (
    '89',
    'Jennifer',
    'Thompson',
    'jennifer.thompson@gmail.com',
    '01334343',
    '1980-12-17',
    17800,
    9000,
    0.5,
    'X4',
    7
  ),
  (
    '90',
    'Lisa',
    'Davis',
    'lisa.davis@gmail.com',
    '01334343',
    '1978-02-07',
    18000,
    39000,
    0.6,
    'X5',
    7
  ),
  (
    '91',
    'David',
    'Walker',
    'david.walker@gmail.com',
    '0132342343',
    '1994-03-09',
    18200,
    33000,
    0.3,
    'X5',
    7
  ),
  (
    '92',
    'Bryan',
    'Franco',
    'bryan.franco@gmail.com',
    '0132342343',
    '1981-10-06',
    18400,
    63000,
    0.5,
    'X2',
    7
  ),
  (
    '93',
    'Wendy',
    'Guzman',
    'wendy.guzman@gmail.com',
    '01323432423',
    '2003-08-23',
    18600,
    78000,
    0.5,
    'X4',
    7
  ),
  (
    '94',
    'Joshua',
    'Faulkner',
    'joshua.faulkner@gmail.com',
    '0132342343',
    '1980-12-17',
    18800,
    33000,
    0.6,
    'X3',
    7
  ),
  (
    '95',
    'David',
    'Mcbride',
    'david.mcbride@gmail.com',
    '0132342343',
    '2012-04-22',
    19000,
    66000,
    0.5,
    'X3',
    7
  ),
  (
    '96',
    'Alexandra',
    'Gentry',
    'alexandra.gentry@gmail.com',
    '01323432423',
    '2012-03-12',
    19200,
    9000,
    0.3,
    'X3',
    7
  ),
  (
    '97',
    'Nathan',
    'Pope',
    'nathan.pope@gmail.com',
    '0132342343',
    '2019-03-14',
    19400,
    66000,
    0.5,
    'X4',
    7
  ),
  (
    '98',
    'Alexis',
    'Lopez',
    'alexis.lopez@gmail.com',
    '01323432423',
    '1980-01-23',
    19600,
    30000,
    0.2,
    'X2',
    7
  ),
  (
    '99',
    'Eric',
    'Neal',
    'eric.neal@gmail.com',
    '0132342343',
    '2009-08-01',
    19800,
    6000,
    0.7,
    'X2',
    7
  ),
  (
    '100',
    'Dylan',
    'Norman',
    'dylan.norman@gmail.com',
    '01334343',
    '1977-09-24',
    20000,
    18000,
    0.2,
    'X2',
    7
  );
