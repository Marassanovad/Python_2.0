import random


def create_list():
    # Вручную создайте список с целыми числами, которые повторяются.
    # Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
    # *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
    my_list = []
    for i in range(10):
        my_list.append(random.randint(0, 10))

    new_list = list(set(my_list))

    new_list_2 = []
    for i in my_list:
        if i not in new_list_2:
            new_list_2.append(i)

    return f"Первый список: {my_list} \nВторой список: {new_list} \nТретий список: {new_list_2}"

def change_line():
    # Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
    # ✔ Целое положительное число
    # ✔ Вещественное положительное или отрицательное число
    # ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
    # ✔ Строку в нижнем регистре в остальных случаях
    user_input = input("Введите данные:")

    if user_input.isdigit():
        return f"Вы вели целое число {user_input}"

    elif user_input.replace(".", "").replace("-", "").isdigit():
        return f"Вы вели вещественное или отрицательное число {user_input}"

    elif user_input.lower() == user_input:
        return f"Вы вели строку в нижнем регистре {user_input}"

    else:
        return f"Вы вели строку с хотя бы одной заглавной буквой {user_input.lower()}"

def create_tuple_and_dict():
    # ✔ Создайте вручную кортеж содержащий элементы разных типов.
    # ✔ Получите из него словарь списков, где: ключ — тип элемента,
    # значение — список элементов данного типа.
    my_tuple = (3, 4.5, 5, False, True, "Test")
    my_dict = {}
    for i in my_tuple:
        if type(i) not in my_dict:
            my_dict[type(i)] = [i]
        else:
            my_dict[type(i)].append(i)
    return f"Кортедж: {my_tuple} \nСловарь: {my_dict}"

def create_list_2():
    # ✔ Создайте вручную список с повторяющимися элементами.
    # ✔ Удалите из него все элементы, которые встречаются дважды.
    my_list = [1,2,3,4,5,2,5,4,4]
    i = 0
    while i < len(my_list):
        if my_list.count(i) == 2:
            my_list.remove(i)
            my_list.remove(i)
        else:
            i += 1
    return my_list

def create_list_3():
    # ✔ Создайте вручную список с повторяющимися целыми числами.
    # ✔ Сформируйте список с порядковыми номерами
    # нечётных элементов исходного списка.
    # ✔ Нумерация начинается с единицы.
    my_list = [1, 2, 3, 4, 5, 6, 7, 7, 4, 3]
    new_list = []
    for i, el in enumerate(my_list, 1):
        if el % 2 != 0:
            new_list.append(i)
    return new_list

def num_stroke():
    # Пользователь вводит строку текста. Вывести каждое слово с новой строки.
    # ✔ Строки нумеруются начиная с единицы.
    # ✔ Слова выводятся отсортированными согласно кодировки Unicode.
    # ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

    text = "Пользователь вводит строку текста. " \
           "Вывести каждое слово с новой строки."
    stroke = text.lower().split(' ')
    stroke.sort()
    max_size = len(max(stroke, key=len))
    for i, elem in enumerate(stroke, 1):
        print(f"{i}. {elem:_>{max_size}}")

def letter_count():
    # ✔ Пользователь вводит строку текста.
    # ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
    # ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
    # ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают
    # или не совпадают в ваших решениях.
    text = "Пользователь вводит строку текста".replace(' ', '').lower()
    my_dict_1 = {}
    for i in set(text):
        my_dict_1[i] = text.count(i)

    my_dict_2 = {}
    for i in text:
        if i not in my_dict_2.keys():
            my_dict_2[i] = 1
        else:
            my_dict_2[i] += 1

    my_dict_3 = {}
    for i in text:
        my_dict_3[i] = my_dict_3.get(i, 0) + 1

    return f'{my_dict_1} \n{my_dict_2} \n{my_dict_3}'


if __name__ == '__main__':
    print(create_list())
    print(change_line())
    print(create_tuple_and_dict())
    print(create_list_2())
    print(create_list_3())
    num_stroke()
    print(letter_count())
