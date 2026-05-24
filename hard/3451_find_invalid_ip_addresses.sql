-- Write your PostgreSQL query statement below
with ip_arrays as (
    select
        ip,
        string_to_array(ip, '.') as ip_array
    from logs
),

ip_ocets as (
    select
        ip,
        ip_array,
        array_length(ip_array, 1) as ip_ocet_len,
        ip_array[1] as first_ocet,
        ip_array[2] as second_ocet,
        ip_array[3] as third_ocet,
        ip_array[4] as fourth_ocet
    from ip_arrays
)

select
    ip, 
    count(*) as invalid_count
from ip_ocets
where (
    first_ocet::integer > 255
    or second_ocet::integer > 255
    or third_ocet::integer > 255
    or fourth_ocet::integer > 255
)
    or (
        left(first_ocet, 1)::integer = 0
        or left(second_ocet, 1)::integer = 0
        or left(third_ocet, 1)::integer = 0
        or left(fourth_ocet, 1)::integer = 0
    )
    or ip_ocet_len != 4
group by 
    ip
order by 
    count(*) desc,
    ip desc