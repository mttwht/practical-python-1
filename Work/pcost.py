# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    'Calculate the total cost of the portfolio'
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total_price = 0
        for row in rows:
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])
                total_price += shares * price
            except ValueError:
                print("Could not convert values", row, "to [str, int, float]")
            
    return total_price

cost = portfolio_cost("Data/portfolio.csv")

print("Total cost:", cost)
