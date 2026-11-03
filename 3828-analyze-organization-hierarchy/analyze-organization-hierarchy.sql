# write your mysql query statement below

with recursive hierarchy as (
    select employee_id, employee_name, manager_id, salary, 1 as level
    from employees
    where manager_id is null

    union all

    select e.employee_id, e.employee_name, e.manager_id, e.salary, h.level + 1
    from employees e
    join hierarchy h
        on e.manager_id = h.employee_id
),

team as (
    select manager_id, employee_id as members
    from employees
    where manager_id is not null

    union all

    select t.manager_id, e.employee_id
    from team t
    join employees e
        on t.members = e.manager_id
),

budget as (
    select
        t.manager_id,
        count(t.members) as team_size,
        sum(e.salary) as salary
    from team t
    join employees e
        on t.members = e.employee_id
    group by t.manager_id
),

output as (
    select
        h.employee_id,
        h.employee_name,
        h.level,
        ifnull(b.team_size, 0) as team_size,
        h.salary+ifnull(b.salary, 0) as budget
    from hierarchy h
    left join budget b
        on h.employee_id = b.manager_id
)

select *
from output
order by level asc, budget desc, employee_name asc;