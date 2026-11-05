from common import *

stages = pd.DataFrame({
    "stage": ["View", "Cart", "Purchase"],
    "sessions": [sf["has_view"].sum(), sf["has_cart"].sum(), sf["purchase_strict"].sum()],
})
views,carts, purchases = stages.loc[0,'sessions'], stages.loc[1, "sessions"], stages.loc[2, "sessions"]
print(stages)
print("\nCart to Purchase pct:", round(100 * purchases / carts, 1))
print("View to Cart pct:", round(100 * carts / views, 1))
print("Abandoned Carts %: ", round(100 * (carts - purchases / carts, 1)))

plt.figure(figsize=(7, 4))
sns.barplot(data=stages, y="stage", x="sessions", color="#4C78A8")
plt.title("Session Funnel: View to Cart to Purchase")
plt.tight_layout() 
plt.show()
