import pandas as pd
import numpy as np
""" commands for pandas columns:
mean 	Average of all values in column
std 	Standard deviation
median 	Median
max 	Maximum value in column
min 	Minimum value in column
count 	Number of values in column
nunique 	Number of unique values in column
unique 	List of unique values in column
"""
orders = pd.read_csv("../data/data_orders.csv")
print(orders.head())
most_expensive = orders["price"].max()
num_colors = orders["shoe_color"].nunique()

"""groupby"""
# df.groupby('column1').column2.measurement()
pricey_shoes = orders.groupby("shoe_type").price.max()
print("pricey_shoes_Series")
print(pricey_shoes)
#print(type(pricey_shoes)) pandas.core.series
pricey_shoes = orders.groupby('shoe_type')["price"].max().reset_index() #ob man hier .price oder ["price"] schreibt -> wie gehabt egal
#macht das ganze zu einem df anstatt einer Series, meistens erwuenscht bei .groupby()
print("pricey_shoes_df")
print(pricey_shoes)
cheap_shoes = orders.groupby("shoe_color").price.apply(lambda x: np.percentile(x,25)).reset_index()
# dies bildet das 25%quantil -> zeigt also den Punkt an, an dem 25% der Schuhe tiefere Kosten haben, und 75% hoehere. (gruppiert nach Schuhfarbe)
print("cheap_shoes")
print(cheap_shoes)
#groupby multiple columns
shoe_counts = orders.groupby(["shoe_type", "shoe_color"]).id.count().reset_index()
print("shoe_counts")
print(shoe_counts)
# Der Prozess ein Dataframe zu "drehen" wird pivoten genannt. Hier kann das ganze fuer den entsprechenden Zweck dienlicher aufbereitet werden.
# In unserem Fall ist es sehr viel sinnvoller, die color gegen den Typ aufzutragen (anstatt lediglich einen index von 0 bis ...), dadurch wird die id, dnn die neuen values
shoe_counts_pivot = shoe_counts.pivot(
    columns='shoe_color',
    index='shoe_type',
    values='id').reset_index()
print("shoe_counts_pivoted")
print(shoe_counts_pivot)

""" pivot vs pivot_table()
pivot_table is a generalization of pivot that can handle duplicate values for one pivoted index/column pair. 
Specifically, you can give pivot_table a list of aggregation functions using keyword argument aggfunc. The default aggfunc of pivot_table is numpy.mean.
pivot_table also supports using multiple columns for the index and column of the pivoted table.
A hierarchical index will be automatically generated for you.
"""