-- Question: What single table can Power BI/Excel load to show the funnel by any segment?
select 'device' as segment_type, device as segment_value,
       count(*) as sessions, sum(has_view) as viewed, sum(has_cart) as carted,sum(purchase_strict) AS purchased
from session_funnel group by device
union all
select 'traffic_source', traffic_source, count(*) as sessions, sum(has_view) as viewed, sum(has_cart) as carted, sum(purchase_strict) as purchased
from session_funnel group by traffic_source
union all
select 'region', region, count(*) as sessions, sum(has_view) as viewed, sum(has_cart) as carted, sum(purchase_strict) as purchased
from session_funnel group by region
union all
select 'is_returning_user', case when is_returning_user = 1 then 'Returning' else 'New' end as segment_value, 
count(*) as sessions, sum(has_view) as viewed, sum(has_cart) as carted, sum(purchase_strict) as purchased
from session_funnel group by is_returning_user;