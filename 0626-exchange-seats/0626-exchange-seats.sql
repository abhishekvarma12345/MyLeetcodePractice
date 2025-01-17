# Write your MySQL query statement below
with final as (
    select count(*) as total
    from Seat
)
select (case 
        when id%2=0 then id-1
        when id=(select total from final) then id
        else id+1 end) as id,
        student
from Seat
order by id
;