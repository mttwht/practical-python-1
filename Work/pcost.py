# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    'Calculate the total cost of the portfolio'
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        total_price = 0
        headers = next(rows)
        for row_number, row in enumerate(rows, start=1):
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])
                total_price += shares * price
            except ValueError:
                print(f"Error at row {row_number}; Could not convert values [{row}] to [str, int, float]")
            
    return total_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("Total cost:", cost)
