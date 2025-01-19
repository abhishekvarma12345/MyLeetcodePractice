# Write your MySQL query statement below
select product_name, sum(unit) as unit
from Products
inner join
(select *
from Orders
where order_date between "2020-02-01" and "2020-02-29") febsold
on Products.product_id = febsold.product_id
group by product_name
having sum(unit) >= 100;