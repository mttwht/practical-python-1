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


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
