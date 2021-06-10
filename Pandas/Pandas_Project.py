import pandas as pd

inventory = pd.read_csv("../data/data_inventory.csv")

print(inventory.head(10))

staten_island = inventory[:10]

# print(staten_island)

product_request = staten_island["product_description"]

seed_request = inventory[(inventory["location"] == "Brooklyn") & (inventory["product_type"] == "seeds")]

# print(seed_request)

inventory["in_stock"] = inventory.apply(lambda x:
                                        True
                                        if x["quantity"] > 0
                                        else False,
                                        axis=1
                                        )

inventory["total_value"] = inventory["quantity"] * inventory["price"]

combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

inventory["full_description"] = inventory.apply(combine_lambda, axis=1)

print(inventory)
