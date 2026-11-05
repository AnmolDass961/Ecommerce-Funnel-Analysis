# E-commerce Funnel & Conversion Analysis

End-to-end funnel analytics project on e-commerce clickstream data, using **SQL**, **Python** and **Power BI**. It finds where sessions drop off between *view → cart → purchase*, which segments convert best and worst, and what the business should fix first.
> Jan–Jun 2025 · 16,045 sessions · 61,323 events · 25 products · 5 categories

---

## Business Problem

Traffic is not the bottleneck, **conversion is**. This project answers:

1. How many sessions make it through each funnel stage, and where is the biggest leak?
2. Which device, traffic source, region and user type convert best and worst?
3. Which categories and products get attention but don't convert?
4. Is conversion stable, rising or falling over time?
5. Are the segment differences statistically significant?
6. Where does the revenue come from?

---

## Key Findings

| Area | Finding |
|---|---|
| Funnel | **7.9%** of sessions purchase; 51.4% add to cart, 15.3% of carts convert |
| Cart abandonment | **84.7%** of cart sessions never purchase (6,987 of 8,253) |
| Device | Desktop **11.8%** vs Mobile **6.5%** vs Tablet **6.1%**; Mobile is ~68% of sessions |
| Traffic source | Direct and Email **10.2%** vs Social **5.8%**; others 6.7–7.6% |
| Category | Fashion cart-to-purchase is the weakest at **10.7%**; Home & Kitchen is the best at 14.2% |
| Revenue | Total **2.04M**; Electronics ≈ 51% of revenue |
| Trend | June sessions rose sharply (~5.6K) while conversion fell to 7.65% |
| Statistics | Device and traffic source are significantly associated with purchase (chi-square, p < 0.05); region is not (p ≈ 0.22) |

### Recommendations

1. **Fix the mobile path to purchase:** one-page checkout, saved payments / wallets, sticky add-to-cart.
2. **Lift Fashion checkout:** size guides, reviews, clear return policy.
3. **Protect and grow Electronics:** financing/EMI messaging, warranty benefits, bundles.
4. **Recover abandoned carts:** cart reminders to known users (Direct and Email are the top converters).

---

## Dashboard Preview

<!-- Add screenshots to /dashboard and update the paths -->
![Product Funnel](dashboard/Product_Funnel.png)
![Conversion Drivers](dashboard/Conversion_Drivers.png)
![Category Performance](dashboard/Category_Performance.png)
![Conclusion](dashboard/Conclusion.png)

---

## Tech Stack

- **SQL (SQLite):** session-level funnel view, segment analysis, CTEs, window functions
- **Python:** pandas, matplotlib, seaborn, scipy 
- **Power BI:** KPI cards, segment and category dashboards

---

## Project Structure

```
.
├── data/                      # events.csv, sessions.csv, products.csv (not committed if large)
├── sql/
│   ├── create_session_funnel_view.sql
│   ├── 02_segment_performance.sql
│   ├── 03_cart_abandonment.sql
│   ├── 04_category_product_attention.sql
│   ├── 05_conversion_trend.sql
│   ├── 06_product_ranking_within_category.sql
│   └── 07_powerbi_segment_table.sql
├── python/
│   ├── common.py              # shared loading / session-level dataframe
│   ├── 01_overall_funnel.py
│   ├── 02_segment_performance.py
│   ├── 03_category_funnel.py
│   ├── 04_conversion_trend.py
│   ├── 05_significance_tests_device_type.py
│   ├── significance_tests_traffic_source_type.py
│   ├── significance_tests_region_wise.py
│   └── 06_revenue.py
├── dashboard/                 # Power BI file (.pbix) and screenshots
├── load_data.py               # loads CSVs into funnel.db (SQLite)
├── requirements.txt
└── README.md
```

---


## Methodology

- **Session funnel view:** each session is flagged `has_view`, `has_cart`, `has_purchase`.
- **`purchase_strict`:** a session counts as a purchase only if it also has a cart event, so the funnel stays consistent.
- **Metrics:**
  - View → Cart % = cart sessions / view sessions
  - Cart → Purchase % = purchase sessions / cart sessions
  - Session conversion % = purchase sessions / all sessions
  - Cart abandonment % = 1 − Cart → Purchase %
- **Significance testing:** chi-square test of independence between each segment and purchase outcome, plus pairwise comparisons (Desktop vs Mobile/Tablet, Direct vs Email, Direct+Email vs others).

---