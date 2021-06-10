import pandas as pd

orders = pd.read_csv('../data/orders.csv')

products = pd.read_csv('../data/products.csv')

customers = pd.read_csv('../data/customers.csv')

print(orders)
print(products)
print(customers)

order_3_description = ""
x = orders.loc[orders["order_id"] == 3, "product_id"]
# print(list(x)[0]) -> ist der Wert
x = list(x)[0]
print(products.loc[products["product_id"] == x])

"""
The .merge method looks for columns that are common between two DataFrames and then looks for rows where those 
column’s values are the same. It then combines the matching rows into a single row in a new table

Inner Merge / Inner join – The default Pandas behaviour, only keep rows where the merge “on” value exists in 
both the left and right dataframes.

Left Merge / Left outer join – (aka left merge or left join) Keep every row in the left dataframe. 
Where there are missing values of the “on” variable in the right dataframe, add empty / NaN values in the result.

Right Merge / Right outer join – (aka right merge or right join) Keep every row in the right dataframe. 
Where there are missing values of the “on” variable in the left column, add empty / NaN values in the result.

Outer Merge / Full outer join – A full outer join returns all the rows from the left dataframe, all the rows 
from the right dataframe, and matches up rows where possible, with NaNs elsewhere.

"""



big_df = orders.merge(customers).merge(products)  # merged erst customers in orders, dann products ins (groeßere) orders

good_stuff = big_df[(big_df["quantity"] >= 2) & (big_df["price"] < 10)]

"""
inner Merge - pandas default, merge function “knew” how to combine tables based on the columns that were the same between two tables. 
For instance, products and orders both had a column called product_id
"""

customers.rename(columns={'customer_id': 'id'})  # default wuerde nicht mehr klappen
"""
test_df = pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'}))  # one way

# Alt.:
pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id')

# If we use this syntax, we’ll end up with two columns called id, one from the first table and one from the second.
# Pandas won’t let you have two columns with the same name, so it will change them to id_x and id_y.

pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id',
    suffixes=['_order', '_customer']
)
# wuerde dieses Problem beheben
"""

orders.loc[8] = [9, 1, 5, 2, "2017-02-01"]

# wuerde beim merge verschwinden:
new_df = orders.merge(products)
#print(new_df)
# da product_id 5 nicht in products vorhanden -> inner merge

new_df = pd.merge(orders, products, how='outer')

print(new_df)
#selbiges Vorgehen fuer left und right merges

"""DataFrames zusammenfuegen:
menu = pd.concat([bakery, ice_cream]) #DF hier selbe Columns
"""