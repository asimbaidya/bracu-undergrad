-- format
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
