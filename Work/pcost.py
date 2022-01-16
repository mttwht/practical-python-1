# pcost.py
#
# Exercise 1.27

f = open("Data/portfolio.csv", 'rt')
headers = next(f).split(',')

total_price = 0

for line in f:
    row = line.split(',')
    name = row[0]
    shares = int(row[1])
    price = float(row[2])
    total_price += shares * price

f.close()

print("Total cost", round(total_price, 2))
    