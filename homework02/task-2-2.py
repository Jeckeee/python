"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

count_list = int(input("Количество элементов списка >>> "))

my_list = []
counter = 0

for el_list in range(count_list):
    my_list.append(input("Новый элемент списка >>> "))
    print(my_list)

for el_rep in range(int(len(my_list) / 2)):
    my_list[counter], my_list[counter + 1] = my_list[counter + 1], my_list[counter]
    counter += 2

print(my_list)
