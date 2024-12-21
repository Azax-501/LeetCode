With employee_earnings as (
    Select d.name as department, e.name as employee, salary
    , dense_rank() over (partition by d.name order by salary desc) as r  
    from employee e
    inner join department d 
    on e.departmentID = d.id
)
Select department, employee, salary
from employee_earnings
where r<=3
order by department, employee;
