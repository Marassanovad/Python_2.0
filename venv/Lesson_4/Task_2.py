# ✔ Напишите функцию для транспонирования матрицы

# Транспонирование матрицы - это операция над матрицей, когда ее строки становятся
# столбцами с теми же номеромами.


def matrix_transposition(matrix):
    '''
    функция для транспонирования матрицы
    '''
    new_matrix = [[0] * len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

def print_matrix(matrix): # этот метод только для проверки что все работает
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()
    print()

if __name__ == '__main__':
    matrix =[[1, 2], [3, 4], [5, 6]]
    matrix_1 = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
    print_matrix(matrix)
    print_matrix(matrix_1)
    new_matrix = matrix_transposition(matrix)
    new_matrix_1 = matrix_transposition(matrix_1)
    print_matrix(new_matrix)
    print_matrix(new_matrix_1)