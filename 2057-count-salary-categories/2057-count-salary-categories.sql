# Write your MySQL query statement below
select "Low Salary" as category, 
        sum(income < 20000) as accounts_count
from Accounts
UNION
select "Average Salary" as category, 
        sum(income BETWEEN 20000 AND 50000) as accounts_count
from Accounts
UNION
select "High Salary" as category, 
        sum(income > 50000) as accounts_count
from Accounts;