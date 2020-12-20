from math import sin, fabs

epsilon = float(input('Введіть точність: '))
x = float(input('x = '))
s = 0  # загальна сума
n = 1

while True:
    current = (2 * (-1) ** (n-1) * sin(n * x)) / n  # поточний доданок
    if fabs(current) >= epsilon:
        s += current
        n += 1
    else:
        break
print('Сума = {0}, Точність = {1}'.format(s, epsilon))


