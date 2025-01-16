# Write your MySQL query statement below
select distinct(l.num) as ConsecutiveNums 
from
(select l1.id, l1.num
from logs l1
inner join
(select (id+1) as id2, num
from logs) l2
on l1.id = l2.id2 and l1.num = l2.num) l
inner join
(select (id+2) as id3, num
from logs) l3
on l.id = l3.id3 and l.num = l3.num;
