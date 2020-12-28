"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def sum_max(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.sort()
    return my_list[-1] + my_list[-2]


print(sum_max(9, 1, 3))
