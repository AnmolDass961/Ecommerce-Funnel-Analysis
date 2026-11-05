# Question: Which categories get attention but don't convert / get removed from carts?
from common import *

piv = events.pivot_table(index="category", columns="event_type",
                         values="event_id", aggfunc="count", fill_value=0)
piv["view_to_cart_%"] = 100 * piv["cart"] / piv["view"]
piv["cart_to_purchase_%"] = 100 * piv["purchase"] / piv["cart"]
piv["removal_%"] = 100 * piv["remove_from_cart"] / piv["cart"]
print(piv.round(2))

plt.figure(figsize=(10, 5))
sns.heatmap(piv[["view_to_cart_%", "cart_to_purchase_%", "removal_%"]], annot=True)
plt.title("Category funnel rates (%)")
plt.tight_layout(); plt.show()
