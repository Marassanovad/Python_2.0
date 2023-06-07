import math
from decimal import Decimal, getcontext
getcontext().prec = 42

# def notation(number, system): # Задания 1. Система счисления
#     RESULT = 0
#     OSTATOK = 0
#     RESULT_STR = ''
#     while True:
#         RESULT = number // system
#         OSTATOK = number % system
#         if RESULT < system:
#             RESULT_STR = RESULT_STR + str(OSTATOK) + str(RESULT)
#             break
#         else:
#             number = RESULT
#             RESULT_STR = RESULT_STR + str(OSTATOK)
#     return RESULT_STR[::-1]


def area_of_the_circle(diametr): # Задания 2. Определения площади и длины окружнасти
    getcontext().prec = 42
    # ROUNDING = 42
    # square = ("Длина окружнасти: ", round(diametr * math.pi, ROUNDING))
    # area = ("Площадь круга: ", round((diametr / 2) ** 2 * math.pi, ROUNDING))
    square = ("Длина окружнасти: ", (Decimal(diametr) * Decimal(math.pi)))
    area = ("Площадь круга: ",(Decimal((diametr / 2) ** 2) * Decimal(math.pi)))
    return square, area


def discriminant():  # Задания 3. Квадратное уравнения
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = b ** 2 - 4 * a * c
    if d >= 0:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        return x1, x2
    else:
        x1 = complex(-b / 2 * a, abs(d)**0.5/(2*a))
        x2 = complex(-b / 2 * a, - abs(d)**0.5/(2*a))
        return x1, x2



if __name__ == '__main__':
    # print(notation(int(input("Введите число: ")), 2))
    # print(area_of_the_circle(10))
    discriminant()


