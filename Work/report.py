# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    'Read a stock portfolio from a file'
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for row in rows:
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])
                holding = {
                    'name': name,
                    'shares': shares,
                    'price': price
				}
                portfolio.append(holding)
            except ValueError:
                print("Could not convert values", row, "to [str, int, float]")
            
    return portfolio


def read_prices(filename):
    'Read stock prices from a file into a dictionary'
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        stocks = {}
        for row in rows:
            try:
                name, price = row[0], float(row[1])
                stocks[name] = price
            except IndexError:
                print("Not enough values in line:", row)
    return stocks



if len(sys.argv) == 3:
    filename1, filename2 = sys.argv[1], sys.argv[2]
else:
    filename1, filename2 = 'Data/portfolio.csv', 'Data/prices.csv'

portfolio = read_portfolio(filename1)
prices = read_prices(filename2)

initial_cost = current_cost = 0.0

for holding in portfolio:
    initial_cost += holding['shares'] * holding['price']
    current_cost += holding['shares'] * prices[holding['name']]

print('Purchase price:', initial_cost)
print('Current value:', current_cost)

print('Gain of', current_cost - initial_cost)
