# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        header = next(f)
        Total = 0.00
        for line in f:
            line = line.split(',')
            cost = int(line[1]) * float(line[2])
            Total += cost
    return Total
    

print(f'Total cost to buy all shares is ${portfolio_cost('Work/Data/portfolio.csv')}')
        
    