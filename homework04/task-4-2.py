"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""


list_one = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_new = [el for el in list_one[1:] if el > list_one[list_one.index(el) - 1]]

print(list_one)
print(list_new)
