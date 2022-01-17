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
        stonks = {}
        for row in rows:
            try:
                name, price = row[0], float(row[1])
                stonks[name] = price
            except IndexError:
                print("Not enough values in line:", row)
    return stonks


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
