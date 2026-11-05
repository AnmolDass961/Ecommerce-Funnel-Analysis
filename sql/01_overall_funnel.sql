-- Question: How many sessions reach each stage, and where is the biggest drop-off?
with t1 as (
    select sum(has_view)     as view_sessions,
           sum(has_cart)     as cart_sessions,
           sum(purchase_strict) as purchase_sessions
    from session_funnel
)
select view_sessions, cart_sessions, purchase_sessions,
       round(100.0 * cart_sessions     / view_sessions, 1) as view_to_cart_pct,
       round(100.0 * purchase_sessions / cart_sessions, 1) as cart_to_purchase_pct,
       round(100.0 * purchase_sessions / view_sessions, 1) as view_to_purchase_pct
from t1;

