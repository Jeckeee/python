"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

while True:
    with open('task-5-5.txt', 'w') as file_txt:
        num_string = input('Введите числа через пробел >>> ')
        file_txt.write(num_string)

    with open('task-5-5.txt') as file_txt_read:
        cont = file_txt_read.readlines()
        for el in cont:
            try:
                print(f'Сумма чисел в файле = {sum(list(map(float, el.strip().split())))}')
                exit()
            except ValueError:
                print('В списке находится не число, повторите попытку!')
