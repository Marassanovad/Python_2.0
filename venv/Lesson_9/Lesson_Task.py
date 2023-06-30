import json
import os.path
from typing import Callable
import random
from functools import wraps

'''
Задание №1
📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
    ○ от 1 до 100 для загадывания,
    ○ от 1 до 10 для количества попыток
📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.


Задание №2
📌 Дорабатываем задачу 1.
📌 Превратите внешнюю функцию в декоратор.
📌 Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
📌 Если не входят, вызывать функцию со случайными числами из диапазонов.


Задание №3
📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.При повторном вызове файл должен расширяться, а не перезаписываться.
📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
📌 Имя файла должно совпадать с именем декорируемой функции.

Задание №4
📌 Создайте декоратор с параметром.
📌 Параметр - целое число, количество запусков декорируемой функции.

Задание №5
📌 Объедините функции из прошлых задач.
📌 Функцию угадайку задекорируйте:
    ○ декораторами для сохранения параметров,
    ○ декоратором контроля значений и
    ○ декоратором для многократного запуска.
📌 Выберите верный порядок декораторов.

Задание №6
📌 Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.
'''

# def outer() -> Callable:  #Задача учителя
#     num_range = int(input('Введите число от 0 до 100: '))
#     attemps = int(input('Введите число от 0 до 10: '))
#     num_sc = random.randint(1, num_range)
#
#     def inner() -> None:
#         nonlocal  num_range, attemps
#         while attemps:
#             print(f'Осталось {attemps} попыток')
#             attemps -= 1
#             num = int(input('Введите число: '))
#             if num == num_sc:
#                 print(f'Вы угадали')
#             else:
#                 advice = ['меньше','больше']
#                 print(f'Ваша число {advice[num > num_sc]} правильного')
#         else:
#             print(f'Вы прогиграли. Правильное число {num_sc}')
#     return inner

def function_closure_guess() -> Callable:
    num = int(input('Введите число от 0 до 100: '))
    count_try = int(input('Введите число от 0 до 10: '))
    num_sc = random.randint(1, num)

    def random_numbers() -> None:
        nonlocal count_try, num_sc
        for i in range(1, count_try + 1):
            user_input = int(input('Введите число: '))
            if num_sc < user_input:
                print("Введите число меньше")
            elif num_sc > user_input:
                print("Введите число больше")
            else:
                print(f'Вы угадали с {i} попытки')
                break
        else:
            print('Вы не угадали')
    return random_numbers

def checked_num(func: Callable):
    @wraps(func)
    def wrapper(count_try: int, num_sc: int):
        num_sc = num_sc if 0 < num_sc < 101 else random.randint(1, 100)
        count_try = count_try if 0 < count_try < 11 else random.randint(1, 10)
        result = func(count_try, num_sc)
        return result
    return wrapper

def writer(file_name):
    def inner_fun(func):
        @wraps(func)
        def wrapper(count_try, num_sc):
            my_dict = {func(count_try, num_sc): [count_try, num_sc]}
            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, indent=3, ensure_ascii=False)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f, indent=3, ensure_ascii=False)
            return my_dict
        return wrapper
    return inner_fun

@writer('file.json')
def func_for_json(*args, **kwargs) -> str:
    ls_for_args = []
    ls_for_kwargs = []
    if args:
        for i in args:
            ls_for_args.append(i)
    if kwargs:
        for key, value in kwargs.items():
            ls_for_kwargs.append(f'{key}={value}')
    return ' '.join(list(map(str, ls_for_args))) + ' '.join(list(map(str, ls_for_kwargs)))

def counter(num):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = []
            for _ in range(num):
                res.append(func(*args, **kwargs))
            return res
        return wrapper
    return deco

# @counter(5)
# def func_for_task4(a, b):
#     return a + b



@counter(2)
@checked_num
@writer('game.json')
# @deco
def game_func(count_try, num_sc) -> None:
    '''
    Функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
    :param count_try: кол-во попыток
    :param num_sc: загаданное число
    :return: None
    '''
    
    print(num_sc)
    while count_try:
        print(f'Осталось {count_try} попыток')
        count_try -=1
        user_input = int(input('Введите число: '))
        if num_sc < user_input:
            print("Введите число меньше")
        elif num_sc > user_input:
            print("Введите число больше")
        else:
            print(f'Вы угадали.Правильное число {num_sc}')
            return num_sc
            # break
    else:
        print(f'Вы не угадали.Правильное число {num_sc}')
        return num_sc
if __name__ == '__main__':
    # print(func_for_json(1, 2, 3, 4, 5, 6, 1))
    # print(func_for_json(tex='1, 2, 3,', text2='4', num=[5, 6, 1]))
    # game_func(10, 110)
    print(f'{game_func.__name__ = }')
    help(game_func)
    # game = outer()
    # game()
    # res = function_closure_guess()
    # res()
    # print(func_for_task4(2,3))
