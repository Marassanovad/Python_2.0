import random as rnd
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга. Программа получает
# на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных
# чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

def empty_desk(length, width): # создает пустую доску
    desk = [[0] * length for i in range(width)]
    return desk

def queen(desk: list, coordinate: tuple):  # проверяет бьют королеву или нет
    a, b = coordinate[0] -1, coordinate[1] -1
    desk[a][b] = 1
    if check_parallel(desk, a, b) and check_diagonal(desk, a, b):
        return True
    else:
        return False

def check_parallel(desk:list, a:int, b:int): # проверка паралелий
    flag = True
    for i in range(len(desk)):
        if desk[a][i] == 1 and i != b:
            flag = False
            return flag
        else:
            flag =True
    for j in range(len(desk[0])):
        if desk[j][b] == 1 and j != a:
            flag = False
            return flag
        else:
            flag = True
    return flag

def check_diagonal(desk, a, b): #проверка диагоналей
    # №1 способ. Почему-то не срабатывает, поэтому пришлось взять abs из интернета
    # for i in range(len(desk)):
    #     if a-i >= 0 and b-i >= 0:
    #         if desk[a-i][b-i] == 1 and a != a - i and b != b -i:
    #             return False
    #     if a + i < len(desk) and b + i < len(desk[0]):
    #         if desk[a + i][b + i] == 1 and a != a + i and b != b + i:
    #             return False

    for i in range(len(desk)):
        for j in range(len(desk[0])):
            if desk[i][j] == 1 and i != a and j != b:
                if abs(a - i) == abs(b - j):
                    return False
    return True

def print_matrix(desk): # вывод доски
    for row in desk:
        for elem in row:
            print(elem, end=' ')
        print()
    print()

def check_desk(desk: list, position: list[tuple]): # проверка всех ферзей
    for el in position:
        if not queen(desk, el):
            return False
    print_matrix(desk)
    return True

def stand_queen(desk): # создания рандомного списка
    correct_possition = []
    while len(correct_possition) < 4:
        possition = (rnd.choice([1,2,3,4,5,6,7,8]), rnd.choice([1,2,3,4,5,6,7,8]))
        if queen(desk, possition):
            correct_possition.append(possition)
    print_matrix(desk)
    return correct_possition






ls =[(5,8), (1,6), (8, 4), (4, 2), (7, 7), (3, 5), (6,3), (2, 1)]
ls2 =[(1,1), (2,3), (3, 5), (4, 4), (8, 2), (4, 4), (6,6), (5, 8)]
ls3 =[(1,1), (2,3), (3, 5), (4, 7), (8, 2), (7, 4), (6,6), (5, 8)]

desk1 = empty_desk(8, 8)
desk2 = empty_desk(8, 8)
desk3 = empty_desk(8, 8)
desk4 = empty_desk(8, 8)

print(check_desk(desk1, ls))
print(check_desk(desk2, ls2))
print(check_desk(desk3, ls3))

ls4 = stand_queen(desk4)
print(ls4)

