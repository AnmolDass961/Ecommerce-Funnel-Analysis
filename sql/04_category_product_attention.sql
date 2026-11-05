-- Question: Which categories and products get attention but don't convert?
--           Which are removed from carts most?
with t1 as (
    select category, product_name,
           sum(case when event_type = 'view'             then 1 else 0 end) as views,
           sum(case when event_type = 'cart'             then 1 else 0 end) as cart_adds,
           sum(case when event_type = 'remove_from_cart' then 1 else 0 end) as removals,
           sum(case when event_type = 'purchase'         then 1 else 0 end) as purchases
    from events_raw
    group by category, product_name
)
select category, product_name, views, cart_adds, removals, purchases,
       round(100.0 * cart_adds / views, 2)     as view_to_cart_pct,
       round(100.0 * purchases /cart_adds, 2) as cart_to_purchase_pct,
       round(100.0 * removals  / cart_adds, 2) as cart_removal_pct
from t1
order by views desc;  

 -- high views + low cart_to_purchase_pct = attention without conversion
