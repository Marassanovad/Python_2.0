import datetime

'''
Задание №1
    📌 Создайте класс Моя Строка, где:
    📌 будут доступны все возможности str
    📌 дополнительно хранятся имя автора строки и время создания (time.time)
    
Задание №2
    📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
    📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
    📌 list-архивы также являются свойствами экземпляра

 Задание №3
    📌 Добавьте к задачам 1 и 2 строки документации для классов.
    
 Задание №4
    📌 Доработаем класс Архив из задачи 2.
    📌 Добавьте методы представления экземпляра для программиста и для пользователя.
      
 Задание №5
    📌 Дорабатываем класс прямоугольник из прошлого семинара.
    📌 Добавьте возможность сложения и вычитания.
    📌 При этом должен создаваться новый экземпляр прямоугольника.
    📌 Складываем и вычитаем периметры, а не длинну и ширину.
    📌 При вычитании не допускайте отрицательных значений.
                    
 Задание №6
    📌 Доработайте прошлую задачу.
    📌 Добавьте сравнение прямоугольников по площади
    📌 Должны работать все шесть операций сравнения
    
'''

class MyStroke(str):
    '''
    Задание №1
    📌 Создайте класс Моя Строка, где:
    📌 будут доступны все возможности str
    📌 дополнительно хранятся имя автора строки и время создания (time.time)
    '''
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.date = datetime.datetime.now()
        return instance

    def __str__(self):
        return f'Имя автора - {self.name}, Время - {self.date}'

    def __repr__(self):
        return f'Для разработчика \nИмя автора - {self.name}, Время - {self.date}'


class Archive:
    '''
    Задание №2
    📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
    📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
    📌 list-архивы также являются свойствами экземпляра
    '''

    _instance = None
    _archive_ls = []

    def __new__(cls, name: str, number: int):
        instance = super().__new__(cls)
        if cls._instance is None:
            cls._instance = instance
        else:
            cls._archive_ls.append(cls._instance)
            cls._instance = instance
        instance.archive_ls = cls._archive_ls.copy()
        return cls._instance

    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.name} {self.number}'

    def __repr__(self):
        return f'{self.name} {self.number}'

class Rectangle:
    '''
     Задание №5
    📌 Дорабатываем класс прямоугольник из прошлого семинара.
    📌 Добавьте возможность сложения и вычитания.
    📌 При этом должен создаваться новый экземпляр прямоугольника.
    📌 Складываем и вычитаем периметры, а не длинну и ширину.
    📌 При вычитании не допускайте отрицательных значений.
    '''

    def __init__(self, length: int, width: int = None):
        self.length = length
        self.width = width if width is not None else length

    def perimeter(self):
        ''' Perimeter'''
        return (self.length + self.width) * 2

    def square(self):
        ''' Square'''
        return self.length * self.width

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
        return f'Длина - {self.length}, Ширина - {self.width}'

    def __repr__(self):
        return f'Длина - {self.length}, Ширина - {self.width}'






if __name__ == '__main__':
    # arc1 = Archive("ffff", 1)
    # arc2 = Archive("ffff", 12)
    # arc3 = Archive("ffff", 14)
    # arc4 = Archive("ffff", 15)
    # print(Archive._archive_ls)
    # print(arc1._archive_ls)
    # help(MyStroke)
    # rec1 = Rectangle(5, 15)
    # rec2 = Rectangle(15, 5)
    # print(rec1 - rec2)
    # print(rec1 < rec2)
    help(Rectangle)


