"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('task-5-1.txt', 'a', encoding='utf-8') as file_txt:
    while True:
        write_str = input('Строка для закписи >>> ')
        if write_str != '':
            file_txt.write(f'{write_str}\n')
        else:
            break
