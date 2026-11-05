# Question: Traffic Source type differences statistically significant?
# H0: Traffic source and purchase outcome are independent.
# H1: They are associated.

from scipy.stats import chi2_contingency
from common import *
ct=pd.crosstab(sf['traffic_source'], sf['purchase_strict'])
chi2, p, _, _ = chi2_contingency(ct)
print(f"\n=== Traffic source ===")
print(ct)
print(f"p-value = {p:.2e}")
print("Reject H0: Traffic source and purchase outcome are associated." if p < 0.05 else "Fail to reject H0: independent.")
# Reject H0: Traffic source and purchase outcome are associated.

# H0: Direct and Email have same purchase rate.
# H1: Direct and Email have different purchase rates.
direct = ct.loc['Direct']
email = ct.loc['Email']
chi2, p, _, _ = chi2_contingency([direct, email])
print(f"\n=== Direct vs Email ===")
print(f"p-value = {p:.2e}")
print("Reject H0: Direct and Email have different purchase rates." if p < 0.05 else "Fail to reject H0: purchase rates are the same.")
# Fail to reject H0: purchase rates are the same.


# H0: Direct + Email has same purchase rate as Others.
# H1: Direct + Email has better purchase rate than Others.
direct_email = direct + email
others=ct.loc[['Organic Search', 'Paid Search', 'Referral','Social']].sum()
chi2, p, _, _ = chi2_contingency([direct_email, others])
print(f"\n=== Direct + Email vs Others ===")
print(f"p-value = {p:.2e}")
print("Reject H0: Direct + Email has better purchase rate than Others." if p < 0.05 else "Fail to reject H0: purchase rates are the same.")
# Reject H0: Direct + Email has better purchase rate than Others.