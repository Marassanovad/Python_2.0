from typing import Callable

def deco():
    '''
    Задание №2

    📌 Дорабатываем задачу 1.
    📌 Превратите внешнюю функцию в декоратор.
    📌 Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
    📌 Если не входят, вызывать функцию со случайными числами из диапазонов.
    '''

def function_closure_guess(count_try: int, num: int) -> Callable[[str], str]:
    '''
    Задание №1

    📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
        ○ от 1 до 100 для загадывания,
        ○ от 1 до 10 для количества попыток
    📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
    '''

    def random_numbers():
        for i in range(1, count_try + 1):
            user_input = input('Введите число: ')
            if int(user_input) == num:
                print(f'Вы угадали с {i} попытки')
                break
        else:
            print('Вы не угадали')
    return random_numbers()

if __name__ == '__main__':
    res = function_closure_guess(2, 10)
    print(type(function_closure_guess), function_closure_guess.__name__)
    print(type(res))
    # , res.__name__)
    # print(res(20))

