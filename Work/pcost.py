# pcost.py
#
# Exercise 1.27

import csv
import sys

from report import read_portfolio

def portfolio_cost(filename):
    '''
    Calculate the total cost of the portfolio
    '''
    portfolio = read_portfolio(filename)
    total_price = 0
    for holding in portfolio:
        total_price += holding['shares'] * holding['price']
    return total_price

def main(argv):
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print("Total cost:", cost)
