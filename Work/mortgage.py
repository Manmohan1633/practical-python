# mortgage.py
#
# Exercise 1.7
principal = 500000.00
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
month = 0
total_paid = 0.00
while principal > 0:
    principal = principal*(1+rate/12)-payment
    month +=1
    if principal <payment + (extra_payment if month <=108 and month>=61 else 0):
        total_paid += principal
        principal = 0
    else:
        total_paid += payment
        if month <=108 and month>=61:
            total_paid +=extra_payment
            principal -=extra_payment
    print(f'It will take {month} to pay toal value of ${total_paid} for principL amount of ${principal}')