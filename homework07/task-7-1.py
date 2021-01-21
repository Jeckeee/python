"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        for el_mat in range(len(self.matrix)):
            for el_cell in range(len(self.matrix[el_mat])):
                self.matrix[el_mat][el_cell] = self.matrix[el_mat][el_cell] + other.matrix[el_mat][el_cell]

        return Matrix.__str__(self)

    def __str__(self):
        for el_mat in self.matrix:
            for el_cell in el_mat:
                print(f'{el_cell:5}', end='')
            print()
        return ''


matrix_1 = [[1, 5, 12], [7, 13, 9], [12, 6, 0]]
matrix_2 = [[8, 11, 5], [3, 4, 18], [15, 8, 2]]

if len(matrix_1) == len(matrix_2):
    for el in range(len(matrix_1)):
        if len(matrix_1[el]) != len(matrix_2[el]):
            print('different matrices')
            exit()
else:
    print('different matrices')
    exit()

result_1 = Matrix(matrix_1)
result_2 = Matrix(matrix_2)

print(result_1 + result_2)
