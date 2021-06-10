from math import log
import numpy as np
from math import sqrt
def calculate_correlation(set_x, set_y):
    # Sum of all values in each dataset
    sum_x = sum(set_x)
    sum_y = sum(set_y)

    # Sum of all squared values in each dataset
    sum_x2 = sum([x ** 2 for x in set_x])

    sum_y2 = 0
    for y in set_y:
        sum_y2 += y ** 2

    # Sum of the product of each respective element in each dataset
    sum_xy = 0
    for i in range(len(set_x)):
        sum_xy += set_x[i] * set_y[i]
    # sum([x*y for x,y in zip(set_x, set_y)]) cleaner

    # Length of dataset
    n = len(set_x)

    # Calculate correlation coefficient
    numerator = n * sum_xy - sum_x * sum_y
    denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

    return numerator / denominator

rate_of_return = 0.075


def display_as_percentage(val):
    return "{:.1f}%".format(val * 100)


print(display_as_percentage(rate_of_return))


def calculate_simple_return(start_price, end_price, dividend=0):
    return (end_price - start_price + dividend) / start_price


simple_return = calculate_simple_return(200, 250, 20)
print('The simple rate of return is ' + display_as_percentage(simple_return) + '%')

""""""


def calculate_log_return(start_price, end_price):
    return (log(end_price) - log(start_price))


log_return = calculate_log_return(200, 250)
print(display_as_percentage(log_return))

daily_return_a = 0.001
monthly_return_b = 0.022

print('The daily rate of return for Investment A is ' + display_as_percentage(daily_return_a))
print('The monthly rate of return for Investment B is ' + display_as_percentage(monthly_return_b))

""""""


def annualize_return(log_return, t):
    return log_return * t


annual_return_a = annualize_return(daily_return_a, 252)
# 252 trading days in a year
print('The annual rate of return for Investment A is ' + display_as_percentage(annual_return_a))

annual_return_b = annualize_return(monthly_return_b, 12)
print('The annual rate of return for Investment B is ' + display_as_percentage(annual_return_b))

""""""

daily_returns = [0.002, -0.002, 0.003, 0.002, -0.001]


# Write code here

def convert_returns(log_returns, t):
    return sum(log_returns) / len(log_returns) * t


annual_return = convert_returns(daily_returns, 252)
print('The annual rate of return is', display_as_percentage(annual_return))

weekly_return = convert_returns(daily_returns, 5)
# weekly_return = sum(daily_returns)
print('The weekly rate of return is', display_as_percentage(weekly_return))

""""""

returns_disney = [0.22, 0.12, 0.01, 0.05, 0.04]
returns_cbs = [-0.13, -0.15, 0.31, -0.06, -0.29]
dataset = [10, 8, 9, 10, 12]


# variance_disney = np.var(returns_disney)
# variance_cbs = np.var(returns_cbs)


def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)
    numerator = 0
    for i in dataset:
        numerator += (i - mean) ** 2
    variance = numerator / len(dataset)
    return variance


variance_disney = calculate_variance(returns_disney)
variance_cbs = calculate_variance(returns_cbs)
print('The variance of Disney stock returns is', variance_disney)
print('The variance of CBS stock returns is', variance_cbs)


def calculate_stddev(dataset):
    variance = calculate_variance(dataset)
    stddev = sqrt(variance)
    return stddev


stddev_disney = calculate_stddev(returns_disney)
stddev_cbs = calculate_stddev(returns_cbs)
print('The standard deviation of Disney stock returns is', display_as_percentage(stddev_disney))
print('The standard deviation of CBS stock returns is', display_as_percentage(stddev_cbs))

returns_general_motors = [0.018, -0.005, -0.047, -0.009, -0.012, 0.003, -0.027, -0.014, 0.029, -0.062, 0.009]
returns_ford = [0.002, -0.004, -0.027, -0.022, -0.001, 0.002, -0.006, -0.017, 0.035, -0.029, 0.002]
returns_exxon_mobil = [0.008, 0.015, 0.009, 0.012, 0.003, -0.007, 0.006, 0.005, -0.048, 0.025, -0.012]
returns_apple = [-0.002, 0.007, -0.004, -0.004, 0.002, 0.013, -0.011, 0.017, -0.001, 0.012, 0.006]

corr_gm_ford = calculate_correlation(returns_general_motors, returns_ford)

print('The correlation coefficient between General Motors and Ford is', corr_gm_ford)

# Write code here
print('The correlation coefficient between General Motors and ExxonMobil is',
      calculate_correlation(returns_general_motors, returns_exxon_mobil))

print('The correlation coefficient between General Motors and Apple is',
      calculate_correlation(returns_general_motors, returns_apple))

corrcoef_matrix = np.corrcoef([returns_general_motors, returns_ford, returns_exxon_mobil, returns_apple])
print(corrcoef_matrix)


def calculate_correlation(set_x, set_y):
    # Sum of all values in each dataset
    sum_x = sum(set_x)
    sum_y = sum(set_y)

    # Sum of all squared values in each dataset
    sum_x2 = sum([x ** 2 for x in set_x])

    sum_y2 = 0
    for y in set_y:
        sum_y2 += y ** 2

    # Sum of the product of each respective element in each dataset
    sum_xy = 0
    for i in range(len(set_x)):
        sum_xy += set_x[i] * set_y[i]
    # sum([x*y for x,y in zip(set_x, set_y)]) cleaner

    # Length of dataset
    n = len(set_x)

    # Calculate correlation coefficient
    numerator = n * sum_xy - sum_x * sum_y
    denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

    return numerator / denominator


""""""
annual_returns = [0.02, 0.05, -0.04, 0.04, 0.02, -0.02, 0.01, 0.03, 0.05, 0.02]

# Write code here
variance = calculate_variance(annual_returns)
stddev = calculate_stddev(annual_returns)
stddev = display_as_percentage(stddev)
annual_returns_percentage = [display_as_percentage(val) for val in annual_returns]
annual_returns_string = ', '.join(annual_returns_percentage)
print('The historical annual rates of return are: ', annual_returns_string)
print('The variance of the rates of return is', variance)
print('The standard deviation of the rates of return is', stddev)
