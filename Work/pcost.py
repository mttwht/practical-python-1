# pcost.py
#
# Exercise 1.27

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
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')
    portfile = argv[1]
    cost = portfolio_cost(portfile)
    print("Total cost:", cost)


if __name__ == '__main__':
    import sys
    main(sys.argv)
