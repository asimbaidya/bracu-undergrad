create table Lab_Grades (
    Std_id varchar(4),
    Name varchar(10),
    Major varchar(3),
    Days_present int,
    Project_marks float,
    CGPA float,
    Sub_date date
);



INSERT INTO `Lab_Grades`(
    `Std_id`,
    `Name`,
    `Major`,
    `Days_present`,
    `Project_marks`,
    `CGPA`,
    `Sub_date`
) VALUES 
('S001', 'Abir', 'CS', 10, 18.5, 3.91, '2018-09-15'),
('S002', 'Nafis', 'CS', 12, 20, 3.86, '2018-08-15'),
('S003', 'Tasneem', 'CS', 8, 18, 3.57, '2018-09-18'),
('S005', 'Arafat', 'CSE', 11, 20, 4.0, '2018-09-13'),
('S006', 'Tasneem', 'CE', 12, 17.5, 3.7, '2018-08-15'),
('S007', 'Muhtadi', 'ECS', 10, 19, 3.67, '2018-09-16');
