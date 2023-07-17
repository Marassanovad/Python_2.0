'''
Задание
📌 Решить задачи, которые не успели решить на семинаре.
📌 Создайте класс студента.
    ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
    ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
    ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
    ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
'''
import csv
from statistics import mean

class Text:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self._validate_name(value)
        setattr(obj, self.param_name, value)

    def _validate_name(self, value):
        if not isinstance(value, str):
            raise AttributeError('Должно быть строкового типа')
        if not value.isalpha():
            raise AttributeError('Должны быть только буквы')
        if not value.istitle():
            raise AttributeError('Должно начинаться с большой буквы')

class Rating:

    def __init__(self, min_value: int = None, max_value: int = None):
        self._min_value = min_value
        self._max_value = max_value

    def __set_name__(self, owner, name):
        self.private_item = '_' + name
        print(self.private_item)

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_item)

    def __set__(self, obj, value: dict):
        self._validate_range(value)
        self._validate_items(value)
        setattr(obj, self.private_item, value)

    def _validate_range(self, value: dict):
        for value in value.values():
            for value_tuple in value:
                if not isinstance(value_tuple, int):
                    raise TypeError(f'Значение {value_tuple} должно быть целым числом')
                if value_tuple is not None and value_tuple < self._min_value:
                    raise ValueError(f'Значение {value_tuple} должно быть больше или равно {self._min_value}')
                if value_tuple is not None and value_tuple > self._max_value:
                    raise ValueError(f'Значение {value_tuple} должно быть меньше или равно {self._max_value}')

    def _validate_items(self, value: dict):
        data = self._load_data()
        valid = 0
        for d in data:
            for v in value:
                if d == v:
                    valid += 1
        if valid != len(value):
            raise AttributeError(f'Предмета нет в списке')

    def _load_data(self):
        data = {}
        file_name = 'school_items.csv'
        i = 0
        with open(file_name, encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for item in csv_reader:
                res = ''.join(item).strip()
                i += 1
                if i != 1:
                    data[res] = None
        return data

class Student:
    name: str = Text()
    surname: str = Text()
    lesson_rating: dict = Rating(2, 5)
    test_rating: dict = Rating(0, 100)

    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._subject: dict[str: tuple] = {}
        self._tests: dict[str: tuple] = {}

    def __str__(self):
        return f'{self._name} {self._surname} \n' \
               f'Оценки по предметам: {self._subject} \n' \
               f'Оценки по тестам: {self._test} \n' \
               f'Средний балл по тестам: {self.average_test_rating()} \n' \
               f'Средний балл по предметам: {self.average_subject_rating()} \n' \
               f'Средний балл по всем предметам: {self.average_subject_rating()} \n'

    def average_test_rating(self):
        avg_res = {}
        for k, v in self._test.items():
            avg_res[k] = round(mean(v), 1)
        return avg_res

    def average_subject_rating(self):
        avg_res = {}
        for k, v in self._subject.items():
            avg_res[k] = round(mean(v), 1)
        return avg_res

    def average_all_rating(self):
        res = 0
        for v in self._subject.values():
            res += mean(v)
        return round((res / len(self._subject.values())), 2)






if __name__ == '__main__':
    student = Student('Li', 'Kim')
    student._subject = {'Физика': (40, 5, 3), 'Биология': (30, 3, 4, 5), 'Математика': (3, 5, 5, 5)}
    student._test = {'Литература': (20, 40, 100), 'Химия': (0, 50, 80)}
    print(student)


