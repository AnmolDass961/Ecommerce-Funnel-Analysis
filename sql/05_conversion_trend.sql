-- Question: Is conversion stable, rising, or falling over time? Are there spikes?

select strftime('%Y-%m', session_date) as year_month,
       count(*) as sessions,
       sum(has_purchase) as purchase_sessions,
       round(100.0 * sum(has_purchase) / count(*), 2) as conversion_pct
from session_funnel
group by year_month
order by year_month;
