# Write your MySQL query statement below
with total_id as (
    select requester_id as id
    from RequestAccepted
    union
    select accepter_id as id
    from RequestAccepted
)
select id, count(id) as num
from RequestAccepted r
inner join
total_id t
on r.requester_id = t.id or r.accepter_id = t.id
where r.accept_date is not null
group by id
order by num DESC
limit 1;