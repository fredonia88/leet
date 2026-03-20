-- Write your PostgreSQL query statement below
with data as (
    select 
        id,
        visit_date,
        people,
        id - row_number() over(order by id) as rownum
    from stadium
    where people >= 100
),

final_data as (
    select
        id,
        visit_date,
        people,
        count(*) over(partition by rownum) as records
    from data
)

select 
    id,
    visit_date,
    people
from final_data
where records >= 3
order by
    visit_date

/*
with data as (
    select
        id,
        visit_date,
        people,
        lag(people) over(order by id asc) as lag_people
    from stadium
),

start_end_rows as (
    select 
        id,
        visit_date,
        people,
        lag_people,
        case when people >= 100 and (lag_people is null or lag_people < 100) then 1 else 0 end as start_row
    from data
    where people >= 100
),

final_data as (
    select 
        id, 
        visit_date,
        people,
        start_row,
        max(case when start_row = 1 then id end) 
            over(order by id rows between unbounded preceding and current row) as first_start_row
    from start_end_rows
)

select
    fd.id,
    fd.visit_date,
    fd.people
from final_data fd
join (
    select
        first_start_row,
        count(*) as records
    from final_data
    group by 
        first_start_row
    having 
        count(*) >= 3
) rd
    on fd.first_start_row = rd.first_start_row
order by 
    visit_date asc
*/