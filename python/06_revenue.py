# Question: Revenue by category, per-session revenue / AOV by segment, and monthly revenue
from common import *

p = events[events["event_type"] == "purchase"]

cat = p.groupby("category").agg(
    revenue=("price", "sum"), 
    units=("price", "size"),
    avg_price=("price", "mean"))

cat["rev_share_%"] = (100 * cat["revenue"] / cat["revenue"].sum()).round(1)
print(cat.sort_values("revenue", ascending=False).round(0), "\n")

rev = p.groupby("session_id")["price"].sum().rename("rev")
sr = sf.merge(rev, on="session_id", how="left").fillna({"rev": 0})

for col in ["device", "traffic_source", "region", "is_returning_user"]:
    t = sr.groupby(col).agg(sessions=("session_id", "count"),
                            revenue=("rev", "sum"),
                            orders=("rev", lambda x: (x > 0).sum()))   
    t["rev_per_session"] = (t["revenue"] / t["sessions"]).round(1)
    t["aov"] = (t["revenue"] / t["orders"]).round(0)
    print(t, "\n")

m = sr.groupby("month").agg(sessions=("session_id", "count"), revenue=("rev", "sum"),
                            orders=("rev", lambda x: (x > 0).sum()))
m["aov"] = (m["revenue"] / m["orders"]).round(0)
print(m)
