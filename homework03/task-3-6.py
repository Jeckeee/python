"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


# Вариант 1
def int_func(update_str):
    return update_str.title()


# Вариант 2
def int_func_1(text):
    return text.title()


def int_func_2(text_str):
    new_text_str = ''
    for el in text_str.split():
        new_text_str += f'{el.title()} '
    return new_text_str


print(f'Вариант 1: {int_func(input("Введите строку >>> "))}\n')

print(f'Вариант 2 (Часть 1): {int_func_1(input("Введите слово >>> "))}\n')
print(f'Вариант 2 (Часть 2): {int_func_2(input("Введите строку >>> "))}\n')


# Вариант 3
cycle = input("Введите строку >>> ")
new_string = ''
for elem in cycle.split():
    new_string += f'{int_func_1(elem)} '

print(f'Вариант 3: {new_string}')



