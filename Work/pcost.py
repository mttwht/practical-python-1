# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    'Calculate the total cost of the portfolio'
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        total_price = 0
        for line in f:
            row = line.split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            total_price += shares * price
            
    return total_price

cost = portfolio_cost("Data/portfolio.csv")

print("Total cost:", cost)
