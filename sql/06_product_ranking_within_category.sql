-- Question: Within each category, which products rank best and worst on conversion?
with t1 as (
    select category, product_name,
           sum(case when event_type = 'cart'     then 1 else 0 end) as cart_adds,
           sum(case when event_type = 'purchase' then 1 else 0 end) as purchases
    from events_raw
    group by category, product_name
),
t2 as (
    select category, product_name,
           round(100.0 * purchases /cart_adds, 2) as cart_to_purchase_pct
    from t1),
t3 as (
    select *, dense_rank() over (partition by category order by cart_to_purchase_pct desc) 
    as rnk
    from t2
),
t4 as (select *, max(rnk) over (partition by category) as max_rnk from t3)
select category, product_name, cart_to_purchase_pct, rnk,
       case when rnk = 1        then 'best_product_conversion_rate'
            when rnk = max_rnk  then 'worst_product_conversion_rate' end as product_status
from t4
where rnk = 1 or rnk = max_rnk
order by category, rnk;
