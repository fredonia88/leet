-- Write your PostgreSQL query statement below
with employees as (
    select 
        id,
        name,
        salary,
        departmentId,
        dense_rank() over(partition by departmentId order by salary desc) as dr
    from employee
)

select 
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
from employees e
join department d 
    on e.departmentId = d.id
where dr <= 3
