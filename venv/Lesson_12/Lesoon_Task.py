import json
from collections import defaultdict


'''
Задание №1
📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
📌 Экземпляр должен запоминать последние k значений.
📌 Параметр k передаётся при создании экземпляра.
📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

 Задание №2
📌 Доработаем задачу 1.
📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

 Задание №3
📌 Создайте класс-генератор.
📌 Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
📌 Если переданы два параметра, считаем step=1.
📌 Если передан один параметр, также считаем start=1.

 Задание №4
📌 Доработайте класс прямоугольник из прошлых семинаров.
📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
📌 Используйте декораторы свойств.


 Задание №5
📌 Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

 Задание №6
📌 Изменяем класс прямоугольника.
📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
'''


class Factorial:

    def __init__(self):
        self.results = defaultdict(list)

    def __call__(self, number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        self.results[number].append(result)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.results.items()))
        return txt

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        new_file = open("manager_file.json", "w", encoding="utf-8")
        json.dump(self.results, new_file, indent=4, ensure_ascii=False)
        new_file.close()


class MyGenarator:

    def __init__(self, *args):
        start, stop, step, result = 1, 1, 1, 1
        if len(args) == 1:
            stop = args[0]
        elif len(args) == 2:
            start = args[0]
            stop = args[1]
        elif len(args) == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        else:
            raise AttributeError

        if start < stop:
            self.start = start
            self.stop = stop
            self.step = step
            self.result = result
            self.iter_step = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.result *= (self.start + self.step * self.iter_step)

        if self.start + self.step * self.iter_step >= self.stop:
            raise StopIteration
        self.iter_step += 1
        return self.result

class Value:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')


def validate(self, value):
    if not isinstance(value, int):
        raise TypeError(f'Значение {value} должно быть целым числом')
    if self.min_value is not None and value < self.min_value:
        raise ValueError(f'Значение {value} должно быть больше 18 или равно {self.min_value}')
    if self.max_value is not None and value >= self.max_value:
        raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Rectangle:

    # __slots__ = ['_length', '_width']

    _length = Range(1)
    _width = Range(1)


    def __init__(self, length: int, width: int = None):
        self._length = length
        self._width = width if width is not None else length

    def perimeter(self):
        ''' Perimeter'''
        return (self._length + self._width) * 2

    def square(self):
        ''' Square'''
        return self._length * self._width

    def __doc__(self):
        return "Документация"

    def __add__(self, other):
        ''' сложения'''
        return self.perimeter() + other.perimeter()

    def __sub__(self, other):
        ''' вычитания '''
        return abs(self.perimeter() - other.perimeter())

    def __eq__(self, other):
        ''' сравнения'''
        return self.square() == other.square()

    def __ne__(self, other):
        ''' сравнения'''
        return self.square() != other.square()

    def __gt__(self, other):
        ''' сравнения'''
        return self.square() > other.square()

    def __ge__(self, other):
        ''' сравнения'''
        return self.square() >= other.square()

    def __lt__(self, other):
        ''' сравнения'''
        return self.square() < other.square()

    def __le__(self, other):
        ''' сравнения'''
        return self.square() <= other.square()

    def __str__(self):
        return f'Длина - {self._length}, Ширина - {self._width}'

    def __repr__(self):
        return f'Длина - {self._length}, Ширина - {self._width}'

    @property
    def length(self):
        self._length = self._length

    @property
    def width(self):
        self._width = self._width

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError

    @wigth.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError


if __name__ == '__main__':
    factor = Factorial()

    factor(1)
    factor(10)
    factor(3)
    factor(2)

    print(factor)
    with factor as new_file:
        new_file(10)

    my_gener = MyGenarator(10, 51, 10)
    for i in my_gener:
        print(i)

