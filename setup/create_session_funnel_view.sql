drop view if exists session_funnel;
create view session_funnel as
with s as (
    select s.session_id, s.user_id, s.session_date, s.device, s.traffic_source,
           s.region, s.is_returning_user,
           max(case when e.event_type = 'view'     then 1 else 0 end) as has_view,
           max(case when e.event_type = 'cart'     then 1 else 0 end) as has_cart,
           max(case when e.event_type = 'purchase' then 1 else 0 end) as has_purchase
    from sessions_raw s
    left join events_raw e on s.session_id = e.session_id
    group by s.session_id, s.user_id, s.session_date, s.device,
             s.traffic_source, s.region, s.is_returning_user)
select *, case when has_cart = 1 and has_purchase = 1 then 1 else 0 end as purchase_strict
from s;