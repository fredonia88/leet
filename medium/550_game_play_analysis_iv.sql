-- Write your PostgreSQL query statement below

with logins as (
    select
        player_id,
        event_date,
        lead(event_date) over(partition by player_id) as next_login_date,
        row_number() over(partition by player_id order by event_date asc) as login_order
    from activity
)

select 
    round(count(distinct case when login_order = 1 and date_trunc('day', event_date) + interval '1 day' = date_trunc('day', next_login_date) then player_id end) / count(distinct player_id)::decimal(10, 4), 2) as fraction
from logins