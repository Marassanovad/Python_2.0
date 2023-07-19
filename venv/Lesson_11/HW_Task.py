
class Matrix:
    '''
    Задание

    📌 Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
    📌 Создайте класс Матрица. Добавьте методы для:
        ○ вывода на печать,
        ○ сравнения,
        ○ сложения,
        ○ *умножения матриц
    '''

    def __init__(self, matrix: list[list[int]]):
        ''' Инициализация '''
        self.matrix = matrix


    def __str__(self):
        ''' Вывод матрицы '''
        res = 'Вывод для пользователя: \n'
        for row in self.matrix:
            for elem in row:
                res += ''.join(f'{elem}\t')
            res += ''.join('\n')
        return res

    def __repr__(self):
        ''' Вывод матрицы '''
        res = 'Вывод для разработчика: \n'
        for row in self.matrix:
            for elem in row:
                res += ''.join(f'{elem}\t')
            res += ''.join('\n')
        return res

    def sum_matrix(self):
        ''' Сумма всех элементов матрицы'''
        res = 0
        for row in self.matrix:
            for elem in row:
                res += elem
        return res

    def __add__(self, other):
        ''' Метод сложения'''
        res = []
        row = []
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                res.append(row)
                row = []
            return Matrix(res)
        else:
            return f'Матрицы разных размеров, сложить не получается'


    def __mul__(self, other):
        ''' Метод умножения'''
        res = []
        row = []
        if len(self.matrix) == len(other.matrix[0]) and  len(other.matrix) == len(self.matrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] * other.matrix[j][i])
                res.append(row)
                row = []
            return Matrix(res)
        else:
            return f'Матрицы разных размеров, умножить не получается'


    ''' Методы сравнения'''
    def __eq__(self, other):
        return self.sum_matrix() == other.sum_matrix()

    def __ne__(self, other):
        return self.sum_matrix() != other.sum_matrix()

    def __gt__(self, other):
        return self.sum_matrix() > other.sum_matrix()

    def __ge__(self, other):
        return self.sum_matrix() >= other.sum_matrix()

    def __lt__(self, other):
        return self.sum_matrix() < other.sum_matrix()

    def __le__(self, other):
        return self.sum_matrix() <= other.sum_matrix()





if __name__ == '__main__':
    matrix = Matrix([[1, 2, 4], [3, 4 , 6], [5, 6, 8]])
    matrix_1 = Matrix([[1, 2, 3], [3, 4, 5]])
    # print(matrix + matrix_1)
    print(matrix >= matrix_1)
    print(matrix)
    print(matrix_1)