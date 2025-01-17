# Write your MySQL query statement below
(select name as results
from MovieRating m
inner join
Users u
on m.user_id = u.user_id
where m.rating is not null
group by m.user_id
order by count(m.user_id) DESC, name ASC
LIMIT 1)
union all
(select title as results
from MovieRating m
inner join
Movies mo
on m.movie_id = mo.movie_id
where m.created_at BETWEEN "2020-02-01" AND "2020-02-29"
group by m.movie_id
order by avg(m.rating) DESC, title ASC
LIMIT 1);

