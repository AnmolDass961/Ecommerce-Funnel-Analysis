# Question: Device type differences statistically significant?
# H0: Device and purchase outcome are independent.  
# H1: They are associated.

from scipy.stats import chi2_contingency
from common import *
ct = pd.crosstab(sf["device"], sf["purchase_strict"])
chi2, p, _, _ = chi2_contingency(ct)
print(f"\n=== Device ===")
print(ct)
print(f"p-value = {p:.2e}")
print("Reject H0: Device and purchase outcome are associated." if p < 0.05 else "Fail to reject H0: independent.")
# Reject H0: Device and purchase outcome are associated.


ct = pd.crosstab(sf["device"], sf["purchase_strict"])
desktop = ct.loc["Desktop"]
mobile = ct.loc["Mobile"]
tablet = ct.loc["Tablet"]

#H0: Desktop and mobile have same purchase rate.
#H1: Desktop has better purchase rate than mobile.
chi2,p,_,_=chi2_contingency([desktop,mobile])
print(f"\n=== Desktop vs Mobile ===")
print(f"p-value = {p:.2e}")
print("Reject H0: Desktop has better purchase rate than mobile." if p < 0.05 else "Fail to reject H0: purchase rates are the same.")
# Reject H0: Desktop has better purchase rate than mobile.

#H0: Desktop and tablet have same purchase rate.
#H1: Desktop has better purchase rate than tablet.
chi2,p,_,_=chi2_contingency([desktop,tablet])
print(f"\n=== Desktop vs Tablet ===")
print(f"p-value = {p:.2e}")
print("Reject H0: Desktop has better purchase rate than tablet." if p < 0.05 else "Fail to reject H0: purchase rates are the same.")
# Reject H0: Desktop has better purchase rate than tablet.