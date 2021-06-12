import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from _mpl_finance import candlestick_ohlc

df = pd.read_csv('data_AAPL_data.csv')
print(df.head())

"""Basic Stock Analysis"""
df['Daily Log Rate of Return'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))

print(df['Daily Log Rate of Return'])

stdev = np.std(df['Daily Log Rate of Return'])
print(stdev)

plt.hist(df['Daily Log Rate of Return'].dropna())
plt.title('Histogram of AAPL Daily Log Rates of Return')
plt.xlabel('Log Rate of Return')
plt.ylabel('Number of Days')
plt.show()

"""Candlestick Chart"""
df['Date'] = pd.to_datetime(df['Date'])
df["Date"] = df["Date"].apply(mdates.date2num)

candle_data = df[['Date', 'Open', 'High', 'Low', 'Close']]
print(candle_data.head())

f1, ax = plt.subplots(figsize=(10, 5))
candlestick_ohlc(ax, candle_data.values, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.title('Candlestick Chart for AAPL')
plt.xlabel('Date')
plt.ylabel('Value($)')
plt.show()

"""
Efficient
Frontier:
print(stock_data.head())
selected = list(stock_data.columns[1:])

returns_quarterly = stock_data[selected].pct_change()
expected_returns = returns_quarterly.mean()
cov_quarterly = returns_quarterly.cov()

random_portfolios = return_portfolios(expected_returns, cov_quarterly)

weights, returns, risks = optimal_portfolio(returns_quarterly[1:])

random_portfolios.plot.scatter(x='Volatility', y='Returns', fontsize=12)
try:
    plt.plot(risks, returns, 'y-o')
except Exception as e:
    print(e)
    pass
plt.ylabel('Expected Returns', fontsize=14)
plt.xlabel('Volatility (Std. Deviation)', fontsize=14)
plt.title('Efficient Frontier', fontsize=24)
plt.show()
"""