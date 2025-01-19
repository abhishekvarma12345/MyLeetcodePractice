# Write your MySQL query statement below
with person_copy as (
    select * from Person
)
delete from Person
where (email, id) not in (
select email, min(id) 
from person_copy
group by email);