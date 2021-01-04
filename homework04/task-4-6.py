"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""


from itertools import count, cycle
from time import sleep

# Задание А
start_num = int(input('Start >>> '))
stop_num = int(input('Stop >>> '))
for el in count(start_num):
    if el > stop_num:
        break
    else:
        print(el)


# Задание Б
start_num = 0
stop_num = int(input('Stop >>> '))
my_list = ['Green', 'Yellow', 'Red']
for el in cycle(my_list):
    if start_num > stop_num:
        break
    print(el)
    sleep(3)
    start_num += 1
