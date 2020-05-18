Create table If Not Exists Employee (Id int, Salary int);
Truncate table Employee;
insert into Employee (Id, Salary) values ('1', '100');
insert into Employee (Id, Salary) values ('2', '200');
insert into Employee (Id, Salary) values ('3', '300');

-- 选择第二高的薪水
select
(select distinct Salary as SecondHighestSalary from Employee order by Salary desc limit 1 offset 1)
as SecondHighestSalary;
