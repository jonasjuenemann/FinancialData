import pandas as pd

ad_clicks = pd.read_csv('../data/data_ad_clicks.csv')

print(ad_clicks.head())

max_by_source = ad_clicks.groupby("utm_source")["user_id"].count().reset_index()

print(max_by_source)

ad_clicks["is_click"] = ~(ad_clicks["ad_click_timestamp"].isnull())
# ~ boolean not for pandas

clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"])["user_id"].count().reset_index()

print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id').reset_index()

print(clicks_pivot)
print(clicks_pivot.columns)

clicks_pivot["percent_clicked"] = clicks_pivot.apply(lambda x: x[True] / (x[False] + x[True]), axis=1)

print(clicks_pivot)

experimental_groups = ad_clicks.groupby(["experimental_group", "is_click"])["user_id"].count().reset_index()

ad_clicks_A = ad_clicks[ad_clicks["experimental_group"] == "A"]
ad_clicks_B = ad_clicks[ad_clicks["experimental_group"] == "B"]

ad_clicks_per_day_A = ad_clicks_A.groupby(["day", "is_click"])["user_id"].count().reset_index()

print(ad_clicks_per_day_A)
A_clicks= ad_clicks_per_day_A.pivot(
    columns='is_click',
    index='day',
    values='user_id').reset_index()
A_clicks["percent_clicked"] = A_clicks.apply(lambda x: x[True] / (x[False] + x[True]), axis=1)
print(A_clicks)

ad_clicks_per_day_B = ad_clicks_B.groupby(["day", "is_click"])["user_id"].count().reset_index()
B_clicks= ad_clicks_per_day_B.pivot(
    columns='is_click',
    index='day',
    values='user_id').reset_index()
B_clicks["percent_clicked"] = B_clicks.apply(lambda x: x[True] / (x[False] + x[True]), axis=1)