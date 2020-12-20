n = int(input('n = '))
x0 = 0
x1 = 7
if n == 0:
    xn = 0
elif n == 1:
    xn = 7
else:
    for i in range(n - 1):
        xn = x1 * (1 + x0)
        x0 = x1
        x1 = xn

print('x({0}) = {1}'.format(n, xn))
