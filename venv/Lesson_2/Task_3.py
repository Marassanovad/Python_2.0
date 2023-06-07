# 3.Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import math
import fractions

def integer_number(fract: str):
    num = fract.split('/')
    return int(num[0]), int(num[1])

def multi(a1: int, a2: int, b1: int, b2: int):
    a = a1 * b1
    b = a2 * b2
    return nod(a, b)

def sum(a1: int, a2: int, b1: int, b2: int):
    if a2 != b2:
        a1 *= b2
        b1 *= a2
        a2 = a2 * b2
    a = a1 + b1
    return nod(a, a2)
    # return a, a2

def nod(a: int , b: int):
    while True:
        if math.gcd(a, b) == 1:
            return f"{a}/{b}"
        else:
            i = math.gcd(a, b)
            a =int(a / i)
            b =int(b / i)

def result(frac1: str, frac2: str):
    a1, a2 = integer_number(frac1)
    b1, b2 = integer_number(frac2)
    res1 = f"{frac1} + {frac2} = {sum(a1, a2, b1, b2)}"
    res2 = f"{frac1} * {frac2} = {multi(a1, a2, b1, b2)}"
    return f"{res1}\n{res2}"


if __name__ == '__main__':
    print(result("2/3", "5/6"))

    f1 = fractions.Fraction(2, 3)
    f2 = fractions.Fraction(5, 6)
    print(f'{f1} + {f2} = {f1 + f2}')
    print(f'{f1} * {f2} = {f1 * f2}')






