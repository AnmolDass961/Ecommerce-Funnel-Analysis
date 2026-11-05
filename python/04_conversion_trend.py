# Question: Is conversion stable, rising, or falling over time? Are there spikes?
from common import *

trend = sf.groupby("month").agg(
    sessions=("session_id", "count"),
    purchases=("purchase_strict", "sum")).reset_index()
trend["conv_pct"] = 100 * trend["purchases"] / trend["sessions"]
print(trend.round(2))

fig, ax1 = plt.subplots(figsize=(9, 4))
ax1.bar(trend["month"], trend["sessions"], color="#C7D3E3")
ax1.set_ylabel("Sessions")
ax2 = ax1.twinx()
ax2.plot(trend["month"], trend["conv_pct"], color="#E45756", marker="o")
ax2.set_ylabel("Conversion %")
plt.title("Monthly sessions and conversion")
plt.tight_layout()
plt.show()
