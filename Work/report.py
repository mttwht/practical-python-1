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
        for row_number, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                name = record['name']
                shares = int(record['shares'])
                price = float(record['price'])
                holding = {
                    'name': name,
                    'shares': shares,
                    'price': price
				}
                portfolio.append(holding)
            except ValueError:
                print(f"Error at row {row_number}; Could not convert values {row} to [str, int, float]")
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


def make_report(portfolio, prices):
    'Produce a report from a portfolio and current stock prices'
    report = []
    for holding in portfolio:
        report.append((
            holding['name'],
            holding['shares'],
            holding['price'],
            prices[holding['name']] - holding['price']
        ))
    return report


if len(sys.argv) == 3:
    filename1, filename2 = sys.argv[1], sys.argv[2]
else:
    filename1, filename2 = 'Data/portfolio.csv', 'Data/prices.csv'

portfolio = read_portfolio(filename1)
prices = read_prices(filename2)
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))

# for r in report:
#     print('%10s %10d %10.2f %10.2f' % r)
for name,shares,price,change in report:
    price = f'${price:0.2f}'
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

initial_cost = current_cost = 0.0

for holding in portfolio:
    initial_cost += holding['shares'] * holding['price']
    current_cost += holding['shares'] * prices[holding['name']]

# print('Purchase price:', initial_cost)
# print('Current value:', current_cost)

# print('Gain of', current_cost - initial_cost)
