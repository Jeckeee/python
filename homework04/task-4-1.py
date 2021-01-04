"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def payment(number_hours, rate_hour, premium):
    return f'Итого начислено: {round((int(number_hours) * int(rate_hour)) + int(premium), 2)} руб.'


if '?' in argv[1:]:
    print('\nПередайте параметры через пробел >>>\n\n'
          '1. Выработка в часах\n'
          '2. Ставка в час\n'
          '3. Премия')
else:
    try:
        number_hours, rate_hour, premium = argv[1:]
        print(payment(number_hours, rate_hour, premium))
    except ValueError:
        print('\nВведите параметры или "?" для просмотра списка параметров >>>')
