-- Write your PostgreSQL query statement below
with data as (
    select
        request_at,
        client_id,
        driver_id,
        status,
        case when status != 'completed' then 1 end as cancelled
    from trips t
    join users u
        on t.client_id = u.users_id
    join users u2
        on t.driver_id = u2.users_id
    where u.banned = 'No'
        and u2.banned = 'No'
        and u.role = 'client'
        and u2.role = 'driver'
        and request_at >= '2013-10-01'
        and request_at <= '2013-10-03'
)

select
    request_at as "Day",
    round(coalesce(sum(cancelled), 0) / count(*)::decimal, 2) as "Cancellation Rate"
from data
group by 
    request_at