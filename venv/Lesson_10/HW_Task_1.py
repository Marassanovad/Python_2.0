from Lesson_Task import *
'''
Задание
📌 Доработаем задачи 5-6. Создайте класс-фабрику.
    ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
    ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
'''

class PetFactory(Dog, Fish, Bird, Animal):
    factory = {Dog: None, Fish: None, Bird: None, Animal: None}


    @classmethod
    def create_animal(cls, name: str = None, breed: str = 'unknown', age: int = 0, animal_type: str='unknown'):
        return Animal(name, breed, age, animal_type)

    @classmethod
    def create_dog(cls, name: str = None, breed: str = 'unknown', age: int = 0, commands: str='unknown'):
        return Dog(name, breed, age, commands)

    @classmethod
    def create_fish(cls, name: str = None, breed: str = 'unknown', age: int = 0, count_fins: int = 0):
        return Fish(name, breed, age, count_fins)

    @classmethod
    def create_bird(cls, name: str = None, breed: str = 'unknown', age: int = 0, count_flights: int = 0):
        return Bird(name, breed, age, count_flights)

    @classmethod
    def add_to_factory(cls, animal):
        cls.factory[type(animal)] = animal

    @classmethod
    def kill_on_the_factory(cls, animal):
        cls.factory.pop(type(animal), 'Их нету')



if __name__ == '__main__':

    dog = PetFactory.create_dog('Kat', 'Husky', commands=['Голос', 'Сидеть'])
    fish = PetFactory.create_fish('Nemo', 'Gold Fish', count_fins=3)
    bird = PetFactory.create_bird('Kesha', 'Parrot', count_flights=2)
    animal = PetFactory.create_animal('Lexa', 'Cat', 12)
    PetFactory.add_to_factory(dog)
    PetFactory.add_to_factory(fish)
    PetFactory.add_to_factory(bird)
    PetFactory.add_to_factory(animal)

    for key, value in PetFactory.factory.items():
        print(f"{key}: {value}")

    PetFactory.kill_on_the_factory(dog)
    # PetFactory.kill_on_the_factory(dog)

    print(PetFactory.factory.get(Dog))

    # for key, value in PetFactory.factory.items():
    #     print(f"{key}: {value}")


