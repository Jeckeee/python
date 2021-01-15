"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task-5-2.txt', encoding='utf-8') as file_txt:
    cont = file_txt.readlines()

    count_str = 1
    for el in cont:
        print(f'В строке № {count_str}: Количество слов - {len(el.strip().split())}')
        count_str += 1

