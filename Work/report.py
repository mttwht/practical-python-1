# report.py
#
# Exercise 2.4

import csv
import sys


def get_filenames():
    '''
    Gets the filenames from arguments if provided, else uses defaults
    '''
    if len(sys.argv) == 3:
        filename1, filename2 = sys.argv[1], sys.argv[2]
    else:
        filename1, filename2 = 'Data/portfolio.csv', 'Data/prices.csv'
    return filename1, filename2

def read_portfolio(filename):
    '''
    Read a stock portfolio from a file
    '''
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
    '''
    Read stock prices from a file into a dictionary
    '''
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
    '''
    Produce a report from a portfolio and current stock prices
    '''
    report = []
    for holding in portfolio:
        report.append((
            holding['name'],
            holding['shares'],
            holding['price'],
            prices[holding['name']] - holding['price']
        ))
    return report

def print_report(report):
    '''
    Print out the report in a tabulated format
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name,shares,price,change in report:
        price = f'${price:0.2f}'
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')


filename1, filename2 = get_filenames()

portfolio = read_portfolio(filename1)
prices = read_prices(filename2)
report = make_report(portfolio, prices)

print_report(report)
