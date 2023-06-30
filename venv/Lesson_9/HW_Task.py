import math
from random import randint as rnd
import csv
from typing import Callable
import json

'''
Задание
📌 Напишите следующие функции:
    ○ Нахождение корней квадратного уравнения
    ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
'''
def find_root_in_every_lines(file_name:str='csv_file.csv'):
    def inner_func(func):
        def wrapper(*args, **kwargs):
            result = {}
            with open(file_name, 'r', encoding='utf-8') as read_file:
                reader = csv.reader(read_file, dialect='excel')
                for i, row in enumerate(reader, 1):
                    a, b, c = row
                    my_dict = {i: {"a": a, "b": b, "c": c, "result": func(int(a), int(b), int(c))}}
                    result.update(my_dict)
                    print(my_dict)
            return result
        return wrapper
    return inner_func


def writer(file_name: str='result.json'):
    def inner_func(func: Callable):
        def wrapper(*args, **kwargs):
            result = func()
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=3, ensure_ascii=False)
            return result
        return wrapper
    return inner_func


@writer('result.json')
@find_root_in_every_lines("csv_file.csv")
def quadratic_equation(a:int, b:int, c:int):
    d = b**2 -(4*a*c)
    if d > 0:
        x1 =((-b) + math.sqrt(d)) / (2*a)
        x2 = ((-b) - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -(b/(2*a))
        return x
    else:
        return 'Нет корней'

def csv_file_with_three_random_numbers(lines:int=100, min:int=-100, max:int=100, file_name:str='csv_file.csv'):
    with open(file_name, 'w', encoding='utf-8', newline='') as write_file:
        writer = csv.writer(write_file, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        for _ in range(lines):
            a = rnd(min, max)
            if a == 0:
                a = 1
            writer.writerow((a, rnd(min, max), rnd(min, max)))


if __name__ == '__main__':
    csv_file_with_three_random_numbers()
    quadratic_equation()






