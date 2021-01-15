"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

dict_ru_number = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре', 5: 'Пять'}
new_file = ''

# В одну строку читается проще?
with open('task-5-4.1.txt', encoding='utf-8') as file_txt:
    for el in file_txt.readlines():
        el_temp = el
        new_file += el_temp\
            .replace(el[:el.find(' ')],
                     dict_ru_number[int(el
                                        .strip()
                                        .replace(' ', '')
                                        .split('—')[1])])

with open('task-5-4.2.txt', 'w', encoding='utf-8') as file_txt_new:
    file_txt_new.write(new_file)
