-- Question: Revenue by category
select category, round(sum(price)) as revenue, count(*) as units,
       round(100.0 * sum(price) / (select sum(price) from events_raw where event_type = 'purchase'), 1) as revenue_share_pct,
       round(avg(price)) as avg_price
from events_raw
where event_type = 'purchase'
group by category
order by revenue desc;

-- Revenue per session & AOV by device
-- (repeat by swapping s.device for s.traffic_source, s.region, s.is_returning_user)
with r as (
    select session_id, sum(price) as rev
    from events_raw
    where event_type = 'purchase'
    group by session_id
)
select s.device,s.traffic_source,s.region,s.is_returning_user,count(*) as sessions,count(r.session_id) as orders,
       round(sum(r.rev)) as revenue,
       round(sum(r.rev) /count(*))            as revenue_per_session,
       round(sum(r.rev) / count(r.session_id), 0) as aov
from sessions_raw s
left join r 
on s.session_id = r.session_id
group by s.device,s.traffic_source,s.region,s.is_returning_user;
