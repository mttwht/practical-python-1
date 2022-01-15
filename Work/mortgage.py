# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    month += 1
    if month <= 12:
        principal -= 1000
        total_paid += 1000

print("Total paid", round(total_paid, 2), "over", month, "months")
