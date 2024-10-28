# mortgage.py
#
# Exercise 1.7
principal = 500000.00
rate = 0.05
payment = 2684.11
extra = 1000.00
month = 0
total_paid = 0.00
while principal > 0:
    principal = principal*(1+rate/12)-payment
    month +=1
    total_paid += payment
    if month <=12:
        total_paid +=extra
        principal -=extra
print(total_paid, month)