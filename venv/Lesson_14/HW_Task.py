import doctest
import unittest
import pytest




class MatrixError(Exception):
    def __init__(self, matrix, other):
        self.col = len(matrix)
        self.row = len(matrix[0])
        self.col1 = len(other)
        self.row1 = len(other[0])

    def __str__(self):
        return f'Матрицы разных размеров. Кол-во столбцов 1- {self.col} 2- {self.col1}. Кол-во строк 1- {self.row} 2- {self.row1}'

class Matrix:
    '''
    ---- Умножение матриц ----
    >>> matrix = Matrix([[1, 2, 4], [3, 4, 6], [5, 6, 8]])
    >>> matrix_1 = Matrix([[1, 2, 3], [3, 4, 5]])
    >>> print(matrix * matrix_1)
    Traceback (most recent call last):
        ...
    MatrixError: Матрицы разных размеров. Кол-во столбцов 1- 3 2- 2. Кол-во строк 1- 3 2- 3

    ---- Сумма всех элементов ----
    >>> matrix = Matrix([[1, 2, 4], [3, 4, 6], [5, 6, 8]])
    >>> print(matrix.sum_matrix())
    39

    ---- Проверка на равенство ----
    >>> matrix = Matrix([[1, 2, 4], [3, 4, 6], [5, 6, 8]])
    >>> matrix_1 = Matrix([[1, 2, 3], [3, 4, 5]])
    >>> print(matrix == matrix_1)
    False
    '''

    def __init__(self, matrix: list[list[int]]):
        ''' Инициализация '''
        self.matrix = matrix

    def matrix_transposition(self):
        '''
        функция для транспонирования матрицы
        '''
        new_matrix = [[0] * len(self.matrix) for i in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                new_matrix[j][i] = self.matrix[i][j]
        return new_matrix


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
            raise MatrixError(self.matrix, other.matrix)


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
            raise MatrixError(self.matrix, other.matrix)


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


''' Unittest'''
class TestFunc(unittest.TestCase):

    def setUp(self):
        self.test_matrix = Matrix([[1, 2, 4], [3, 4, 6], [5, 6, 8]])
        self.test_matrix_1 = Matrix([[1, 2, 3], [3, 4, 5]])

    def test1(self):
        self.assertTrue(self.test_matrix != self.test_matrix_1)

    # def test2(self): # не поняла как должно работать
    #     self.assertRaises(MatrixError, , self.test_matrix, self.test_matrix_1)

    def test3(self):
        self.assertTrue(self.test_matrix > self.test_matrix_1)

    def test4(self):
        self.assertFalse(self.test_matrix < self.test_matrix_1)

'''Pytest'''
@pytest.fixture
def data1():
    return Matrix([[1, 2, 4], [3, 4, 6], [5, 6, 8]])

@pytest.fixture
def data2():
    return Matrix([[1, 2, 3], [3, 4, 5]])

def test_1(data1):
    assert data1.matrix_transposition()

def test_2(data1, data2):
    with pytest.raises(MatrixError):
        assert data1 + data2

def test_3(data1, data2):
    assert data1 >= data2

def test_4(data1, data2):
    assert not data1 <= data2


if __name__ == '__main__':
    unittest.main(verbosity=2)
    doctest.testmod(verbose=True)
    # pytest.main([ '-v'])