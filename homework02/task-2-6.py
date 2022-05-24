"""
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
"""


list_product = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}),
    (4, {'название': 'видеокарта', 'цена': 7800, 'количество': 13, 'eд': 'шт.'}),
    # (5, {'название': 'провод', 'цена': 100, 'количество': 2000, 'eд': 'м.'})
]


list_param = []
list_name = []


for elem in list_product:
    for el_key in elem[1].keys():
        if el_key in list_param:
            continue
        else:
            list_param.append(el_key)


for el_param in list_param:
    list_temp_name = []
    for el_prod in list_product:
        for key, value in el_prod[1].items():
            if key == el_param:
                list_temp_name.append(value)
    list_name.append(list_temp_name)


dict_analytics = {}
counter = 0
for key in list_param:
    dict_analytics[key] = list_name[counter]
    counter += 1

print(dict_analytics)






