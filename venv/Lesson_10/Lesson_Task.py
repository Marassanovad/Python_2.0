import math as m
import random as rnd


class Circle:
    '''
    Задание №1

    📌 Создайте класс окружность.
    📌 Класс должен принимать радиус окружности при создании экземпляра.
    📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
    '''
    def __init__(self, radius: int):
        self.radius = radius

    def return_circumference(self):
        return m.pi * (2 * self.radius)

    def square(self):
        return m.pi * (self.radius ** 2)

class Rectangle:
    '''
    Задание №2

    📌 Создайте класс прямоугольник.
    📌 Класс должен принимать длину и ширину при создании
    экземпляра.
    📌 У класса должно быть два метода, возвращающие периметр и площадь.
    📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
    '''

    def __init__(self, length: int, width: int = None):
        self.length = length
        self.width = width if width is not None else length

    def perimeter(self):
        return (self.length + self.width) * 2

    def square(self):
        return self.length * self.width

class Person:
    '''
    Задание №3
    📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
    📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
    📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
    '''
    def __init__(self, name: str=None, surname: str=None, age: int=0, gender: str=None):
        self.name = name
        self.surname = surname
        self.__age = age
        self.gender = gender
        
    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age +=1

    def full_name(self):
        return f'{self.surname} {self.name}'

    def __str__(self):
        return f'{self.surname} {self.name} {self.gender} {self.__age}'

class Employee(Person):
    '''
    Задание №4
    📌 Создайте класс Сотрудник.
    📌 Воспользуйтесь классом человека из прошлого задания.
    📌 У сотрудника должен быть:
        ○ шестизначный идентификационный номер
        ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
    '''
    def __init__(self, name: str = None, surname: str = None, age: int = 0, gender: str = None, profession: str = None):
        super().__init__(name, surname, age, gender)
        self.profession = profession
        self._id = rnd.randint(100000, 999999)
        # self._access_level = Employee.access_level(self)

    @property
    def access_level(self):
        sum = 0
        # str_id - str(self.id)
        # list_id_numbers = sum(list(map(int, str_id)))
        # return list_id_numbers % 7
        for num in str(self._id):
            sum += int(num)
        return sum % 7

    def __str__(self):
        return f'{self.access_level} {self._id}'

'''
Задание №5
📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

Задание №6
📌 Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки.
'''

class Animal:
    def __init__(self, name: str = None, breed: str = 'unknown', age: int = 0, animal_type: str='unknown'):
        self.name = name
        self.breed = breed
        self.age = age
        self.animal_type = animal_type

    def __str__(self):
        return f'{self.name}, {self.breed}, {self.age}'

    def print_specific(self):
        return f'Специфические данные'

class Dog(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', age: int = 0, commands: list[str] = 'unknown'):
        super().__init__(name, breed, age)
        # self.name = name
        # self.breed = breed
        self.commands = commands

    def __str__(self):
        return f'{self.name}, {self.breed}, {self.age}, {self.commands}'

    def print_specific(self):
        return f'{self.commands}'


class Fish(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', age: int = 0, count_fins: int = 0):
        super().__init__(name, breed, age)
        # self.name = name
        # self.breed = breed
        self.count_fins = count_fins

    def __str__(self):
        return f'{self.name}, {self.breed}, {self.age}, {self.count_fins}'

    def print_specific(self):
        return f'{self.count_fins}'

class Bird(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', age: int = 0, count_flights: int = 0):
        super().__init__(name, breed, age)
        # self.name = name
        # self.breed = breed
        self.count_flights = count_flights

    def __str__(self):
        return f'{self.name}, {self.breed}, {self.age}, {self.count_flights}'

    def print_specific(self):
        return f'{self.count_flights}'

if __name__ == '__main__':
    dog = Dog('Kat', 'Husky', ['Голос', 'Сидеть'])
    print(type(dog))
    # fish = Fish('Nemo', 'Gold Fish', 3)
    # bird = Bird('Kesha', 'Попугай', 2)
    # animal = Animal('Lexa', 'Cat', 12)
    # print(animal.print_specific())
    # print(dog.print_specific())
    # print(fish.print_specific())
    # print(bird.print_specific())



    # h1 = Person('Sasha', 'Kim', 18, 'm')
    # h2 = Person('Masha', 'Won', 24, 'f')
    # e1 = Employee('Masha', 'Won', 24, 'f')
    # print(e1)
    # print(h1)
    # print(h2)
    # h2.birthday()
    # print(h2.get_age())
    # print(h1.full_name())