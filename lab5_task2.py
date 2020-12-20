x = int(input('x = '))
y = int(input('y = '))


def count_of_zeros(number):
    count = 0
    while number > 0:
        if number % 10 == 0:
            count += 1
        number = number // 10
    return count


if count_of_zeros(x) > count_of_zeros(y):
    print('Найбільшу кількість 0 містить: {0}'.format(x))
else:
    print('Найбільшу кількість 0 містить: {0}'.format(y))


