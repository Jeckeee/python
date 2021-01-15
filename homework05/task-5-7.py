"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""

import json

dict_profit = {}
dict_loss = {}
dict_ave_profit = {}

with open('task-5-7.txt', encoding='utf-8') as file_txt:
    for el in file_txt.readlines():
        el_split = el.strip().split(';')
        proceeds = float(el_split[2]) - float(el_split[3])
        if proceeds > 0:
            dict_profit[el_split[0]] = proceeds
        else:
            dict_loss[el_split[0]] = proceeds
    dict_ave_profit['average_profit'] = \
        round(sum(dict_profit.values()) / len(dict_profit))

with open('task-5-7.json', 'w') as file_json_dump:
    json.dump([dict_profit, dict_loss, dict_ave_profit], file_json_dump)

with open('task-5-7.json') as file_json_load:
    data = json.load(file_json_load)
    print(data)
    print(type(data))
