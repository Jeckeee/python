"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict.
"""

month_num = int(input("Введите номер месяца >>> "))

dict_season = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}
list_season = ('Зима', 'Весна', 'Лето', 'Осень')


if month_num == 12 or 1 <= month_num <= 2:
    print(dict_season.get(0))
    print(list_season[0])
elif 3 <= month_num <= 5:
    print(dict_season.get(1))
    print(list_season[1])
elif 6 <= month_num <= 8:
    print(dict_season.get(2))
    print(list_season[2])
elif 9 <= month_num <= 11:
    print(dict_season.get(3))
    print(list_season[3])
else:
    print("Ошибка! Введите номер месяца от 1 до 12 >>> ")
