-- Write your PostgreSQL query statement below
with min_date as (
    select 
        min(visited_on) + interval '6 days' as mdate
    from customer
),

amount_by_day as (
    select
        visited_on,
        sum(amount) as amount
    from customer
    group by 
        visited_on
),

data as (
    select
        visited_on,
        sum(amount) over(order by visited_on range between interval '6 days' preceding and current row) as amount,
        round(avg(amount) over(order by visited_on range between interval '6 days' preceding and current row), 2) as average_amount
    from amount_by_day
)

select 
    data.*
from data, min_date md
where visited_on >= md.mdate
order by 
    visited_on asc