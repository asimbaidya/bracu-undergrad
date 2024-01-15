-- 1
Select
  min(CGPA)
from
  Lab_Grades;

-- 2
Select
  count(*) as total_students,
  avg(Project_marks) as average_project_marks
from
  Lab_Grades;

-- 3
Select
  sum(Days_Present)
from
  Lab_Grades;

-- 4
Select
  major,
  min(CGPA) as minCGPA,
  max(CGPA) as maxCGPA
from
  Lab_Grades
group by
  major;

-- 5
Select
  major,
  count(*)
from
  Lab_Grades
group by
  major;

-- 6
Select
  major,
  min(CGPA) as minCGPA,
  max(CGPA) as maxCGPA
from
  Lab_Grades
group by
  major
having
  count(*) >= 2;

-- 7
Select
  major,
  min(CGPA) as minCGPA,
  max(CGPA) as maxCGPA
from
  Lab_Grades
where
  sub_date <= '2018-09-15'
group by
  major;

-- Sub/Nested Query
-- 8
Select
  Name
from
  Lab_Grades
where
  Project_marks = (
    Select
      max(Project_marks)
    from
      Lab_Grades
  );

-- 9
Select
  Major,
  Name,
  Days_present
from
  Lab_Grades
where
  (Major, Days_present) in (
    Select
      Major,
      min(Days_present)
    from
      Lab_Grades
    group by
      Major
  );

-- 10
Select
  *
from
  Lab_Grades
where
  Major = 'CSE'
  and CGPA > any (
    Select
      CGPA
    from
      Lab_Grades
    where
      Major = 'CS'
  );

-- 11
Select
  *
from
  Lab_Grades
where
  Major = 'CSE'
  and CGPA > all (
    Select
      CGPA
    from
      Lab_Grades
    where
      Major = 'CS'
  );

-- coorelated-sub-query
-- 12
Select distinct
  Major
from
  Lab_Grades L1
where
  exists (
    Select
      *
    from
      Lab_Grades L2
    where
      L2.Major = L1.Major
      and L2.CGPA < 3.7
  );

-- 13
Select
  Name
from
  Lab_Grades L1
where
  not exists (
    Select
      *
    from
      Lab_Grades L2
    where
      L2.Std_ID != L1.Std_ID
      and L2.Project_marks > L1.Project_marks
  );

-- 14
Select
  Name
from
  Lab_Grades L1
where
  not exists (
    Select
      *
    from
      Lab_Grades L2
    where
      L2.Std_ID != L1.Std_ID
      and L2.Project_marks >= L1.Project_marks
  );

--  15
Select
  Count(*)
from
  Lab_Grades L1
where
  not exists (
    Select
      *
    from
      Lab_Grades L2
    where
      L2.Std_ID != L1.Std_ID
      and L2.Project_marks > L1.Project_marks
  );

-- 16
Select
  Count(*)
from
  Lab_Grades
where
  Project_marks = (
    Select
      max(Project_marks)
    from
      Lab_Grades
  );

-- 17
Select
  Count(*)
from
  Lab_Grades
where
  Project_marks >= all (
    Select
      Project_marks
    from
      Lab_Grades
  );

-- 18
Select
  Major
from
  Lab_Grades
group by
  Major
having
  Count(*) >= all (
    Select
      Count(*)
    from
      Lab_Grades
    group by
      Major
  );
