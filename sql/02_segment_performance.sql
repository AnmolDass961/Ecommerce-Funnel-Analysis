-- Question: Which device, traffic source, region, or user type converts best and worst?
-- Device
select device, count(*) as sessions,
       sum(has_cart) as cart_sessions, sum(purchase_strict) as purchase_sessions,
       round(100.0 * sum(has_cart)     / sum(has_view), 1) as view_to_cart_pct,
       round(100.0 * sum(purchase_strict) / sum(has_cart), 1) as cart_to_purchase_pct,
       round(100.0 * sum(purchase_strict) / count(*), 1) as session_conversion_pct
from session_funnel 
group by device;

-- Traffic source
select traffic_source, count(*) as sessions,
       sum(has_cart) as cart_sessions, sum(purchase_strict) as purchase_sessions,
       round(100.0 * sum(has_cart)     / sum(has_view), 1) as view_to_cart_pct,
       round(100.0 * sum(purchase_strict) / sum(has_cart), 1) as cart_to_purchase_pct,
       round(100.0 * sum(purchase_strict) / count(*), 1) as session_conversion_pct
from session_funnel 
group by traffic_source;

-- Region
select region, count(*) as sessions,
       sum(has_cart) as cart_sessions, sum(purchase_strict) as purchase_sessions,
       round(100.0 * sum(has_cart)     / sum(has_view), 1) as view_to_cart_pct,
       round(100.0 * sum(purchase_strict) / sum(has_cart), 1) as cart_to_purchase_pct,
       round(100.0 * sum(purchase_strict) / count(*), 1) as session_conversion_pct
from session_funnel 
group by region;

-- User type (new vs returning)
select is_returning_user, count(*) as sessions,
       sum(has_cart) as cart_sessions, sum(purchase_strict) as purchase_sessions,
       round(100.0 * sum(has_cart)     / sum(has_view), 1) as view_to_cart_pct,
       round(100.0 * sum(purchase_strict) / sum(has_cart), 1) as cart_to_purchase_pct,
       round(100.0 * sum(purchase_strict) / count(*), 1) as session_conversion_pct
from session_funnel 
group by is_returning_user;
