"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

string_input = "Пополнить рейтинг (да) или (нет)? >>> "
list_rating = [7, 5, 3, 3, 2, 8]

print(f"Рейтинг: {list_rating}")
append_elem = input(string_input)


while True:

    if append_elem.lower() == 'да':
        new_number = int(input("Введите число >>> "))
        list_rating.append(new_number)
        list_rating.sort()
        list_rating.reverse()
        print(f"Новый рейтинг: {list_rating}")
        append_elem = input("Пополнить рейтинг? >>> ")
    elif append_elem.lower() == 'нет':
        print(f"Ввод рейтинга закончен! Рейтинг: {list_rating}")
        break
    else:
        print("Ошибка ввода. Введите значение (да) или (нет)!")
        append_elem = input(string_input)
