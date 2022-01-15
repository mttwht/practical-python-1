# mortgage.py
#
# Exercise 1.7

# user variables
from os import sep


extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0


print("month", "total paid", "remaining principal", sep='\t')

while principal > 0:
    month += 1
    monthly_payment = payment
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        monthly_payment += extra_payment
    principal = principal * (1 + rate / 12) - monthly_payment
    total_paid = total_paid + monthly_payment
    print(month, round(total_paid, 2), round(principal, 2), sep='\t')

print()
print("Total paid", round(total_paid, 2), "over", month, "months")
