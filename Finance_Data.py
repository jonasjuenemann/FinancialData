import pandas_datareader as dr
import pandas as pd
from pandas_datareader import wb, tsp
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
import pandas_datareader.data as web
from datetime import datetime

"""
Google Finance, yahoo! web reader (for stock prices, derivatives)
federal research (fred), worldbank, OECD (for global economics data)
"""


"""Data-reader module"""
start = datetime(2005, 1, 1)
end = datetime(2008, 1, 1)
indicator_id = 'NY.GDP.PCAP.KD'

gdp_per_capita = wb.download(indicator=indicator_id, start=start, end=end, country=['US', 'CA', 'MX'])

#print(gdp_per_capita)

symbols = get_nasdaq_symbols()

print(symbols)

start = datetime(2019, 1, 1) # year, month, day
end = datetime(2019, 2, 1)

 #web.DataReader(‘MORTGAGE30US’, ‘fred’, start_date, end_date)
#'MORTGAGE30US' - An identifier provided by the API specifying the data we want back, in this case 30 year mortgage data in the US
#'fred' - The name of the API we want to access
sap_data = web.DataReader("SP500", "fred", start, end)

print(sap_data)

"""API Keys"""
"""
In some cases you’ll pass the API key directly into the pandas-datareader function you’re using to access the API.

Other times you’ll be required to set the API key as a more secure operating system (os) environment variable like with the quandl API below:
os.environ["QUANDL_API_KEY"] = "demo" # set APIkey as os env variable
df = web.DataReader('AAPL.US', 'quandl', start, end)
"""
my_api_key = "example"

#dr.get_data_tiingo('GOOG', api_key=my_api_key)

"""Dataframe shifts"""

# shifts all rows down by 1
#dataframe.shift(1);
# shifts all rows in name column up 5
#dataframe['name'].shift(-5);
# shifts all rows in the price column down 3
#dataframe['price'].shift(3);

start = datetime(2008, 1, 1)
end = datetime(2018, 1, 1)

gdp = web.DataReader("GDP", "fred", start, end)
#print(gdp) #Daten alle 3 Monate
# Werte außerhalb des Index verschwinden (keine neuen Indexes generiert.), neue "leere" Columns werden mit nan gefuellt.
# print(gdp["GDP"].shift(1))
gdp['growth'] = gdp['GDP'] - gdp['GDP'].shift(1)
#print(gdp)

"""Calculating Basic Financial Statistics"""

# tsp_data = tsp.TSPReader(start,end).read() funktioniert nicht ordentlich
# print(tsp_data.var())
# print(tsp_data.cov())

apple_prices = pd.read_csv("data/data_apple_prices.csv")
print(apple_prices["open"].var())

gas_prices = web.DataReader("APUS12A74714", "fred", start, end)
print(gas_prices)