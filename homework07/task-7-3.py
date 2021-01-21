"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки
определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return f'Итог сложения клеток: {self.count + other.count}'

    def __sub__(self, other):
        result = self.count - other.count
        if result > 0:
            return f'Итог вычитания клеток: {result}'
        else:
            return 'Разность двух клеток меньше нуля'

    def __mul__(self, other):
        return f'Итог умножения клеток: {self.count * other.count}'

    def __truediv__(self, other):
        return f'Итог деления клеток: {round(self.count / other.count)}'

    def make_order(self, value):
        row = ''
        for el in range(int(self.count / value)):
            row += f'{"*" * value}\\n'
        if self.count >= value:
            row += f'{"*" * (self.count % value)}'
            return row
        else:
            return f'Количество ячеек в рябу больше количество ячеек в клетке!'


cell_1 = Cell(22)
cell_2 = Cell(17)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_1.make_order(3))
print(cell_2.make_order(4))





