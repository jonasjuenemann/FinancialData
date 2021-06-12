import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = 'data/data_stock_data.csv'
stock_data = pd.read_csv(path)

print(stock_data.head())

# Average returns of asset
selected = list(stock_data.columns[1:])
quarterly_returns = stock_data[selected].pct_change()
# print(quarterly_returns)
expected_returns = quarterly_returns.mean()
print(expected_returns)

# Weight of an asset
weight_nike = 3 / 10
weight_ua = 2 / 10
weight_skechers = 5 / 10

# For Simplicity: returns of Nike,UA,Skechers
ret_nike = 1.4
ret_ua = 0.8
ret_skechers = 7

test_return = weight_nike * ret_nike + weight_ua * ret_ua + weight_skechers * ret_skechers
print('The expected return is equal to {:.2f}%'.format(test_return))

# Covariance:
returns_cov = quarterly_returns.cov()
print(returns_cov)

from _rf import return_portfolios, optimal_portfolio

random_portfolios = return_portfolios(expected_returns, returns_cov)
print(random_portfolios.head().round(4))

plt.scatter(x=random_portfolios["Volatility"], y=random_portfolios['Returns'])
plt.xlabel('Volatility (Std. Deviation)')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier')
plt.show()

# print(quarterly_returns[1:])
weights, returns, risks = optimal_portfolio(quarterly_returns[1:])

plt.scatter(x=random_portfolios["Volatility"], y=random_portfolios['Returns'])
plt.plot(risks, returns, 'y-o')
plt.xlabel('Volatility (Std. Deviation)')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier')
plt.show()

path = 'data_stock_data_nvidia.csv'

stock_data = pd.read_csv(path)
selected = list(stock_data.columns[1:])

returns_quarterly = stock_data[selected].pct_change()
expected_returns = returns_quarterly.mean()
cov_quarterly = returns_quarterly.cov()


single_asset_std = np.sqrt(np.diagonal(cov_quarterly))
df = return_portfolios(expected_returns, cov_quarterly)
weights, returns, risks = optimal_portfolio(returns_quarterly[1:])

plt.scatter(x=random_portfolios["Volatility"], y=random_portfolios['Returns'], fontsize=12)
plt.plot(risks, returns, 'y-o')
plt.scatter(single_asset_std, expected_returns, marker='X', color='red', s=200)
for xc in single_asset_std:
    plt.axvline(x=xc, color='red')

if 'nvidia' in path:
    plt.axvline(single_asset_std[-1], color='green')
    plt.scatter(single_asset_std[-1], expected_returns[-1], marker='X', color='green', s=200)
    original_EF = np.genfromtxt("data_stock_risks_return.csv", delimiter=',')
    plt.plot(risks, returns, 'g-o')
    plt.plot(original_EF[:, 0], original_EF[:, 1], 'y-o')
plt.ylabel('Expected Returns', fontsize=14)
plt.xlabel('Volatility (Std. Deviation)', fontsize=14)
plt.title('Efficient Frontier', fontsize=24)
plt.show()
