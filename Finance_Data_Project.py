import pandas as pd
import pandas_datareader as web
import pandas_datareader.wb as wb  # world bank
import numpy as np
from datetime import datetime

gold_prices = pd.read_csv("data_gold_prices.csv")

crude_oil_prices = pd.read_csv("data_crude_oil_prices.csv")

# print(type(gold_prices["Date"][0])) -> str

start = datetime(1999, 1, 1)
end = datetime(2019, 1, 1)

nasdaq_data = web.DataReader("NASDAQ100", "fred", start, end)
sap_data = web.DataReader("SP500", "fred", start, end)
# high level economic data like GDP
gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start=start, end=end)
# and the total value of goods and services exported in a given year.
export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start=start, end=end)


def log_return(prices):
    return np.log(prices / prices.shift(1))


# reversed das Dataframe, Datum jetzt aufsteigend.
gold_prices = gold_prices.reindex(index=gold_prices.index[::-1])
crude_oil_prices = crude_oil_prices.reindex(index=crude_oil_prices.index[::-1])

gold_returns = log_return(gold_prices["Gold_Price"])
crudeoil_returns = log_return(crude_oil_prices["Crude_Oil_Price"])
sap_returns = log_return(sap_data["SP500"])
nasdaq_returns = log_return(nasdaq_data["NASDAQ100"])
gdp_returns = log_return(gdp_data["NY.GDP.MKTP.CD"])
export_returns = log_return(export_data["NE.EXP.GNFS.CN"])

print("Summe, Varianz")
print("Gold")
print(gold_returns.sum(), gold_returns.var())
print("Öl")
print(crudeoil_returns.sum(), crudeoil_returns.var())
print("S&P500")
print(sap_returns.sum(), sap_returns.var())
print("Nasdaq")
print(nasdaq_returns.sum(), nasdaq_returns.var())
