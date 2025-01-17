# Write your MySQL query statement below
select user_id, CONCAT(UCASE(LEFT(name, 1)), LCASE(SUBSTR(name, 2))) name
from Users
order by user_id;