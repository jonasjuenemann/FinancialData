import pandas as pd

visits = pd.read_csv('../data/visits.csv', parse_dates=[1])
cart = pd.read_csv('../data/cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('../data/checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('../data/purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = pd.merge(
    visits,
    cart,
    how="left")
# Number of Visitors who DIDNT put anything in their cart
null_values_carts = visits_cart.cart_time.isna().sum()
print(null_values_carts/len(visits_cart.cart_time))

cart_checkout = pd.merge(
    cart,
    checkout,
    how="left")
# Number of Visitors who DID put something in their cart, but DIDNT checkout
null_values_checkout = cart_checkout.checkout_time.isna().sum()
print(null_values_checkout/len(cart_checkout.checkout_time))

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
true_checkout = all_data.checkout_time.notna().sum()
true_purchase = all_data.purchase_time.notna().sum()
print(1 - true_purchase/true_checkout)
# Number of Visitors who DID put something in their cart and DID checkout, but didnt

checkout_purchase = pd.merge(
    checkout,
    purchase,
    how="left")
null_values_purchase = checkout_purchase.purchase_time.isna().sum()
print(null_values_purchase/len(checkout_purchase.purchase_time))
# Number of Visitors who DID put something in their cart and DID checkout, but didnt
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print(all_data.time_to_purchase.dropna())
print(all_data.time_to_purchase.mean())