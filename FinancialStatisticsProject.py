from utils import *
from math import log, sqrt


def calculate_log_return(start_price, end_price):
    return (log(end_price) - log(start_price))

def display_as_percentage(val):
    return "{:.1f}%".format(val * 100)

def convert_returns(log_returns, t):
    return sum(log_returns) / len(log_returns) * t

def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)
    numerator = 0
    for i in dataset:
        numerator += (i - mean) ** 2
    variance = numerator / len(dataset)
    return variance

def calculate_stddev(dataset):
    variance = calculate_variance(dataset)
    stddev = sqrt(variance)
    return stddev

def calculate_correlation(set_x, set_y):
  sum_x = sum(set_x)
  sum_y = sum(set_y)

  sum_x2 = sum([x ** 2 for x in set_x])
  sum_y2 = sum([y ** 2 for y in set_y])

  sum_xy = sum([x * y for x, y in zip(set_x, set_y)])

  n = len(set_x)

  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

  return numerator / denominator


amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52,
                 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]


def get_returns(prices):
    returns = []
    for i in range(len(prices[:-1])):
        returns.append(calculate_log_return(prices[i], prices[i + 1]))
    return returns

def calculate_stddev(dataset):
    variance = calculate_variance(dataset)
    stddev = sqrt(variance)
    return stddev


amazon_returns = get_returns(amazon_prices)
ebay_returns = get_returns(ebay_prices)
print([display_as_percentage(x) for x in amazon_returns])
print(convert_returns(amazon_returns, 12))
print(display_as_percentage(convert_returns(ebay_returns, 12)))
print(calculate_variance(amazon_returns))
print(calculate_variance(ebay_returns))
print(display_as_percentage(calculate_stddev(amazon_returns)))
print(display_as_percentage(calculate_stddev(ebay_returns)))
print(display_as_percentage(calculate_correlation(amazon_returns, ebay_returns)))