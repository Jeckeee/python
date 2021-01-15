"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

counter_line = 1
dict_courses = {}
with open('task-5-6.txt', encoding='utf-8') as file_txt:
    for el in file_txt.readlines():
        try:
            el_split = el.strip().split(':')
            count_hour = 0
            courses = el_split[0]
            list_count_hour = el_split[1].split()
            for elem in list_count_hour:
                try:
                    count_hour += int(elem[:elem.find('(')])
                except ValueError:
                    pass
            dict_courses[courses] = count_hour
        except IndexError:
            print(f'Строка № {counter_line} исключена из расчета, отсутствует знак < : > после названия курса!')
        counter_line += 1
print(dict_courses)
