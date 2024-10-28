# bounce.py
#
# Exercise 1.5
height = 100
hits =0
while hits<10:
    hits+=1
    height = height*(3/5)
    height = round(height,4)
    print(hits, height)