from math import cos

n = int(input('n = '))
x = float(input('x = '))
s = 0
for i in range(1, n+1):
    s += cos(x)**i
print('Sum = {0}'.format(s))
