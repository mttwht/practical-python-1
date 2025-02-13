# report.py
#
# Exercise 2.4

from fileparse import parse_csv


def read_portfolio(filename):
    '''
    Read a stock portfolio from a file
    '''
    with open(filename, 'rt') as file:
        portfolio = parse_csv(file,
                              select=['name', 'shares', 'price'],
                              types=[str, int, float])
    return portfolio

def read_prices(filename):
    '''
    Read stock prices from a file into a dictionary
    '''
    with open(filename, 'rt') as file:
        stocks = parse_csv(file,
                           types=[str, float],
                           has_headers=False)
    return dict(stocks)

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

def portfolio_report(filename1, filename2):
    '''
    Prints a report generated from a portfolio and a current price file
    '''
    portfolio = read_portfolio(filename1)
    prices = read_prices(filename2)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)


if __name__ == '__main__':
    import sys
    main(sys.argv)
