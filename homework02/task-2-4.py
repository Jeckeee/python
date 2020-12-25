"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. 
Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове.
"""


string = input("Введите строку >>> ")

list_string = string.split()
counter = 1

for el_list in list_string:
    if len(el_list) <= 10:
        print(f"{counter}. {el_list}")
        counter += 1
    else:
        print(f"{counter}. {el_list[0:10]}")
        counter += 1
