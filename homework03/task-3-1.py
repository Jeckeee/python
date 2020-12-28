"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def get_division(divisible, divider):
    try:
        return round(divisible / divider, 2)
    except ZeroDivisionError:
        return 'Деление на ноль!'


num_1 = float(input('Введите делимое >>> '))
num_2 = float(input('Введите делитель >>> '))

print(get_division(num_1, num_2))
