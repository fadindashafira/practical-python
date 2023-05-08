# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05 # 5 %
monthly_payment = 2684.11
total_paid = 0.0
month = 0
extra = 1000.0

extra_payment_start_month = 61
extra_payment_end_month = 108

# Calculate total amount that Dave will have
# to pay over the ife of the mortgage:

while principal > 0:
    month += 1
    principal = principal * (1+rate/12) - monthly_payment
    total_paid = total_paid + monthly_payment
    
    # if months <= 12:
    #     principal = principal - extra
    #     total_paid = total_paid + extra

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra
        total_paid = total_paid + extra
    
    # if principal < 0:
    #     principal = principal - principal
    #     total_paid = total_paid + principal
    print(f'{month} {total_paid:.2f} {principal:.2f}')
    # print(month, round(total_paid,2), round(principal, 2))

print('Total paid', round(total_paid,2))
print('Months', month)