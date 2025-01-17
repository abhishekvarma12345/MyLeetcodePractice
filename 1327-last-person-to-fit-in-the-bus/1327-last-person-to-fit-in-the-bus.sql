# Write your MySQL query statement below
select s.person_name
from
(select turn, person_name, @running_total := @running_total + weight as cumWeight
from Queue
join (select @running_total := 0) t
order by turn) s
where s.cumWeight <= 1000
order by s.cumWeight DESC
LIMIT 1;