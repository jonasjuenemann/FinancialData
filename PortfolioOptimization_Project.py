import pandas as pd
import matplotlib.pyplot as plt
from _rf import return_portfolios, optimal_portfolio
import numpy as np

# 1. Load the stock data
stock_data = pd.read_csv("data/data_stock_data2.csv")
# weak<2
print(stock_data.head())
# 2. Find the quarterly return for each period
returns_quarterly = stock_data[list(stock_data.columns[1:])].pct_change()
# Column fuer Datum ausgeschlossen, erste Spalte nur nan's

# 3. Find the expected returns
expected_returns = returns_quarterly.mean()

# 4. Find the covariance
cov_quarterly = returns_quarterly.cov()

# 5. Find a set of random portfolios
random_portfolios = return_portfolios(expected_returns, cov_quarterly)

# 6. Plot the set of random portfolios
plt.scatter(x=random_portfolios["Volatility"], y=random_portfolios["Returns"])

# 7. Calculate the set of portfolios on the EF
weights, returns, risks = optimal_portfolio(returns_quarterly[1:])

# 8. Plot the set of portfolios on the EF
plt.plot(risks, returns, color="orange", marker="o")
plt.ylabel('Expected Returns', fontsize=14)
plt.xlabel('Volatility (Std. Deviation)', fontsize=14)
plt.title('Efficient Frontier', fontsize=24)

# Compare the set of portfolios on the EF to the
# add a Line for the "old" weak, portfolio distribution
# (Werte fuer risks und returns werden hier nicht neu ausgerechnet, lediglich uebernommen aus csv),
# koennte hier mit der optimal_portfolio Funktion auch berechnet werden
weak_EF = pd.read_csv('data/data_weak_risk_returns.csv')
plt.plot(weak_EF['Risks'], weak_EF['Returns'], 'g-o')

# Cutting the two stocks with the highest negative return (ChesapeakeE and GE)
strong_EF = pd.read_csv('data/data_strong_risk_returns.csv')
plt.plot(strong_EF['Risks'], strong_EF['Returns'], 'k-x')
# Doesnt improve anything, since these assets had low returns and were correlated to
# other assets in the portfolio

try:
    single_asset_std = np.sqrt(np.diagonal(cov_quarterly))
    # Array der Standardabweichungen der Kurse (die Diagonale von oben links nach unten rechts gibt ja
    # jeweils die Varianz des entsprechenden Objekts an)
    plt.scatter(single_asset_std, expected_returns, marker='X', color='red', s=200)  # s-> size
    for xc in single_asset_std:
        plt.axvline(x=xc, color='red')
except:
    pass
plt.show()

path = 'data/data_stock_data3.csv'

# 1. Load the stock data
stock_data = pd.read_csv(path)
selected = list(stock_data.columns[1:])
# print(stock_data[selected].pct_change().mean())
# print(stock_data[selected].pct_change().cov())

# stock_names = ['PFE', 'TGT', 'M', 'VZ', 'JPM', 'MRO', 'KO', 'PG', 'CVS', 'HPQ']
selected = ['PFE', 'CVS', 'M', 'VZ', 'JPM']
# JPM -> highest return
# VZ -> smalles correlation to JPM
# M, CVS, PFE -> next highest returns

# 2. Find the quarterly for each period
returns_quarterly = stock_data[selected].pct_change()

# 3. Find the expected returns
expected_returns = returns_quarterly.mean()

# 4. Find the covariance
cov_quarterly = returns_quarterly.cov()

# 5. Find a set of random portfolios
random_portfolios = return_portfolios(expected_returns, cov_quarterly)

# 6. Plot the set of random portfolios
random_portfolios.plot.scatter(x='Volatility', y='Returns', fontsize=12)

# 7. Calculate the set of portfolios on the EF
weights, returns, risks = optimal_portfolio(returns_quarterly[1:])

# 8. Plot the set of portfolios on the EF
plt.plot(risks, returns, 'y-o')
plt.ylabel('Expected Returns', fontsize=14)
plt.xlabel('Volatility (Std. Deviation)', fontsize=14)
plt.title('Efficient Frontier', fontsize=24)

# nur beim ersten mal benutzen, (wenn die selected Leiste auskommentiert ist)
# pd.DataFrame({'Risks': risks, 'Returns': returns}).to_csv('all_ten.csv', index=False)

# 9. Compare the set of portfolios on the EF to the
single_asset_std = np.sqrt(np.diagonal(cov_quarterly))
plt.scatter(single_asset_std, expected_returns, marker='X', color='red', s=200)

# All 10
all_ten_EF = pd.read_csv('data/all_ten.csv')
plt.plot(all_ten_EF['Risks'], all_ten_EF['Returns'], 'g-o')
plt.show()
