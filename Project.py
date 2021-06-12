import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import pandas_datareader as web
import pandas_datareader.data as data
from datetime import datetime
from _rf import *

start = datetime(2017, 10, 1)
end = datetime(2020, 10, 1)
# importing the data
# for google Finance: data_source= "google"
"""
AMD, NVDA, GOOG, MSFT, AMZN, ADBE, DPZ, 0700.HK (Tencent), TSLA, V, INTC

ETFs: IQQH.DE, ESP0.DE
Clean Energy, VideoGames, 
Index: ^NDX, ^GDAXI
Nasdaq, Dax, 
"""

symbols = ["AMD", "NVDA", "GOOG", "MSFT", "AMZN", "ADBE", "DPZ", "0700.HK", "TSLA", "V", "INTC"]

# stock_data = data.DataReader(symbols, 'yahoo', start, end)
stock_data = web.get_data_yahoo(symbols, start, end)
stock_data = stock_data["Adj Close"]
# stock_data_amd = stock_data["AMD"]

plt.figure(figsize=(20, 20))
plt.plot(stock_data.index, stock_data)
plt.legend(["AMD", "NVDA", "GOOG", "MSFT", "AMZN", "ADBE", "DPZ", "Tencent", "TSLA", "V", "INTC"])
plt.title("Stocks Adjusted Price")
plt.xlabel("Date")
plt.ylabel("Adjusted Closing Price Over Time")
plt.savefig("FinanceProject.jpg")
plt.show()

plt.figure(figsize=(20, 20))
ax1 = plt.subplot(4, 3, 1)
ax2 = plt.subplot(4, 3, 2)
ax3 = plt.subplot(4, 3, 3)
ax4 = plt.subplot(4, 3, 4)
ax5 = plt.subplot(4, 3, 5)
ax6 = plt.subplot(4, 3, 6)
ax7 = plt.subplot(4, 3, 7)
ax8 = plt.subplot(4, 3, 8)
ax9 = plt.subplot(4, 3, 9)
ax10 = plt.subplot(4, 3, 10)
ax11 = plt.subplot(4, 3, 11)
ax1.plot(list(stock_data.index), stock_data["AMD"])
# hier auf dem ax object, muessen wir set_title anstatt .title() machen
ax1.set_title("AMD")
ax2.plot(list(stock_data.index), stock_data["NVDA"])
ax2.set_title("Nvidia")
ax3.plot(list(stock_data.index), stock_data["GOOG"])
ax3.set_title("Google")
ax4.plot(list(stock_data.index), stock_data["MSFT"])
ax4.set_title("Microsoft")
ax5.plot(list(stock_data.index), stock_data["AMZN"])
ax5.set_title("Amazon")
ax6.plot(list(stock_data.index), stock_data["ADBE"])
ax6.set_title("Adobe")
ax7.plot(list(stock_data.index), stock_data["DPZ"])
ax7.set_title("Dominos")
ax8.plot(list(stock_data.index), stock_data["0700.HK"])
ax8.set_title("Tencent")
ax9.plot(list(stock_data.index), stock_data["TSLA"])
ax9.set_title("Tesla")
ax10.plot(list(stock_data.index), stock_data["V"])
ax10.set_title("Visa")
ax11.plot(list(stock_data.index), stock_data["INTC"])
ax11.set_title("Intel")
plt.savefig("FinanceProjectMultiPlot.jpg")
plt.show()

d_ror = stock_data.pct_change()
# print(sum(list(stock_data.isna().sum())))  # halbwegs viele: 214 insgesamt
# print(d_ror.isna().sum())  # nur noch 1 pro column
d_ror_mean = d_ror.mean()
colors = ["green" if i >= 0.002 else "red" if i <= 0.001 else "blue" for i in d_ror_mean]
plt.bar(list(d_ror_mean.index), d_ror_mean, color=colors)
plt.title("Mean RoR per Stock")
plt.show()
d_ror_var = d_ror.var()
plt.bar(list(d_ror_var.index), d_ror_var)
plt.title("Var per Stock")
plt.show()
d_ror_cov = d_ror.cov()
d_ror_corr = d_ror.corr()
"""
Strongest Rate of Return: AMD, Tesla
Schwaechste Korrelationen der beiden: Tencent, Dominos
"""

"""
# Bilden der Mean-Variance Portfolio Optimization
random_portfolios = return_portfolios(d_ror_mean, d_ror_cov)
plt.scatter(x=random_portfolios["Volatility"], y=random_portfolios["Returns"])
weights, returns, risks = optimal_portfolio(d_ror[1:])
#plt.plot(risks, returns, color="orange", marker="o")
plt.ylabel('Expected Returns', fontsize=14)
plt.xlabel('Volatility (Std. Deviation)', fontsize=14)
plt.title('Efficient Frontier', fontsize=24)
plt.show()
Funktioniert nicht, da an einer Stelle vermutlich die Wurzel einer negativen Zahl gezogen werden muss
"""

SmallerPortfolio = stock_data[["AMD", "TSLA", "0700.HK", "DPZ"]]
d_ror = SmallerPortfolio.pct_change()
d_ror_mean = d_ror.mean()
d_ror_cov = d_ror.cov()
