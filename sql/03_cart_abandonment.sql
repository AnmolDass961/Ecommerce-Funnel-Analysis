-- Question: Of the sessions that added to cart, how many never purchased?
select sum(has_cart) as cart_sessions,
       sum(case when has_cart = 1 and has_purchase = 0 then 1 else 0 end) as abandoned_sessions,
       round(100.0 * sum(case when has_cart = 1 and has_purchase = 0 then 1 else 0 end)
             / sum(has_cart), 1) as abandoned_sessions_pct
from session_funnel;
