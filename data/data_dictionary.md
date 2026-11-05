# Data Dictionary

## events.csv.gz
| Column | Meaning |
|---|---|
| event_id | Unique synthetic event identifier |
| event_time | Event timestamp |
| event_type | view, cart, remove_from_cart, purchase |
| product_id | Product identifier |
| product_name | Product name |
| category | Product category |
| brand | Synthetic brand |
| price | Listed item price; purchase rows may include a small discount |
| user_id | Synthetic user identifier |
| session_id | Synthetic session identifier |
| device | Mobile, Desktop, Tablet |
| traffic_source | Organic Search, Paid Search, Social, Email, Direct, Referral |
| region | Synthetic broad region |
| event_date | Event date |

## sessions.csv
One row per session. Includes session start, dimensions, counts of views/cart additions/purchase items, and a session conversion flag.

## products.csv
One row per product with product_id, product_name, category, brand, and list_price.
