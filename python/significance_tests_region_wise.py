from common import *
from scipy.stats import chi2_contingency

# H0: Region and purchase outcome are independent.
# H1: They are associated.
ct=pd.crosstab(sf['region'], sf['purchase_strict'])
chi2, p, _, _ = chi2_contingency(ct)
print(f"\n=== Region ===")
print(ct)
print(f"p-value = {p:.2e}")
print("Reject H0: Region and purchase outcome are associated." if p < 0.05 else "Fail to reject H0: independent.")
# Fail to reject H0: Region and purchase outcome are independent.,pval=0.22