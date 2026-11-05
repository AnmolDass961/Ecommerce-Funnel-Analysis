# Question: Which device, traffic source, region converts best and worst?
from common import *
def seg_table(col):
    t = sf.groupby(col).agg(
        sessions=("session_id", "count"),
        carts=("has_cart", "sum"),
        purchases=("purchase_strict", "sum")).reset_index()
    t['view_to_cart_pct'] = (t["carts"] * 100 / t["sessions"]).round(2)
    t["cart_to_purchase_pct"] = (t["purchases"] * 100 / t["carts"]).round(2)
    t['session_conversion_rate'] = (t["purchases"] * 100 / t["sessions"]).round(2)
    return t.sort_values("cart_to_purchase_pct", ascending=False)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for ax, col in zip(axes, ["device", "traffic_source", "region"]):
    t = seg_table(col)
    print(t, "\n")
    sns.barplot(x=col, y="cart_to_purchase_pct", data=t, ax=ax, color="#4C78A8")
    ax.set_title(f"Purchase Rate by {col}")
    ax.set_ylabel("Cart to Purchase rate")
    ax.tick_params(axis="x", rotation=30)
plt.tight_layout()
plt.show()
