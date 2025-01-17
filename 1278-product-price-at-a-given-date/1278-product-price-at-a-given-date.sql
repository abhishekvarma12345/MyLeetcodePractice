# Write your MySQL query statement below
with id_date_less as 
(select product_id, new_price as price
from Products
where (product_id, change_date) in
(select product_id, max(change_date) as max_change_date_before
from Products
where change_date <= DATE("2019-08-16")
group by product_id))
select * 
from id_date_less
union
select distinct(product_id) as product_id, 10 as price 
from Products
where product_id not in (
    select product_id
    from id_date_less
);