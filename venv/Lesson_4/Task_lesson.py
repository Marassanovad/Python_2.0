
def break_a_string(data: str):
    """
    Задача №1

    ✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
    ✔ Строки нумеруются начиная с единицы.
    ✔ Слова выводятся отсортированными согласно кодировки Unicode.
    ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
    """
    txt = ""
    data = "Пользователь вводит строку текста. " \
           "Вывести каждое слово с новой строки."
    stroke = data.lower().split(' ')
    stroke.sort()
    max_size = len(max(stroke, key=len))
    for i, elem in enumerate(stroke, 1):
        txt += f"{i}. {elem:_>{max_size}}\n"
    return txt

def sorted_unicod(text: str):
    """
    Задача №2

    ✔ Напишите функцию, которая принимает строку текста.
    ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.
    """
    my_list = []
    for i in text:
        if ord(i) not in my_list:
            my_list.append(ord(i))
    my_list.sort()
    return my_list

def dict_unicod(stroke: str):
    """
    Задача №4
    
    ✔ Функция получает на вход строку из двух чисел через пробел.
    ✔ Сформируйте словарь, где ключом будет
    символ из Unicode, а значением — целое число.
    ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
    """
    my_dict = {}

    start, end =map(int, stroke.split())
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        my_dict[chr(i)] = i
    return my_dict

def sort_spisok(spisok: list):
    """
    Задача №4

    ✔ Функция получает на вход список чисел.
    ✔ Отсортируйте его элементы in place без использования
    встроенных в язык сортировок.
    ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
    """
    for i in range(len(spisok)):
        for j in range(len(spisok) - 1 - i):
            if spisok[j] > spisok[j + 1]:
                spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]

def work_list(names: list[str], salarys: list[int], premiums: list[float]):
    dict_of_premies = {}
    """
    Задача №5
    
    Функция принимает на вход три списка одинаковой длины:
        ✔ имена str,
        ✔ ставка int,
        ✔ премия str с указанием процентов вида «10.25%».
    Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
    Сумма рассчитывается как ставка умноженная на процент премии.
    """
    if len(names) == len(salarys) == len(premiums):
        for name, salary, premium in zip(names, salarys, premiums):
            dict_of_premies[name] = [salary / 100 * premium]
        return dict_of_premies
    else:
        return False

def list_and_two_index(list_of_numbers: list, first_index: int, second_index: int):
    """
    Задача №6

    ✔ Функция получает на вход список чисел и два индекса.
    ✔ Вернуть сумму чисел между между переданными индексами.
    ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

    """

    if len(list_of_numbers) < first_index < 0:
        first_index = 0
    if 0 < second_index < len(list_of_numbers):
        second_index = len(list_of_numbers)

    return sum(list_of_numbers[first_index + 1: second_index - 1])

def company(comp: dict):
    """
    Задача №7

    ✔ Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами
    (3-10 чисел) в качестве значения.
    ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину,
    а если хотя бы одна убыточная — ложь.
    """

    for name_company, value in comp.items():
        summa = 0
        for money in value:
            summa += money
        if summa < 0:
            return False
    return True

def delete_s(endings: str):
    """
    Задача №8

    ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
    ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
    оканчивающихся на s (кроме переменной из одной буквы s) на None.
    ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
    """
    for var in globals().copy():
        if not var.startswith('__'):
            if var.endswith(endings):
                if len(var) > 1:
                    new_name = var[:-1]
                    globals()[new_name] = None
                else:
                    globals()[var] = globals().get(var)



if __name__ == '__main__':
    list_for_sorted = [9, 1, 34, 76, 5, 12, 92, 1]
    names = ["Tasha", "Kolya", "Misha"]
    salarys = [120_000, 100_000, 90_000]
    premiums = [10.2, 11.5, 50]
    company_dict = {'rosa': (122345, -2345564, 234454),
                    'new_company': (22222, 22222, 222222),
                    'big_digit': (111111, 11111, 1111)}
    sas = "qas"
    a = 12
    s = 5.4
    asad = True
    adsss = False


    # print(break_a_string("Пользователь вводит строку текста. Вывести каждое слово с новой строки."))
    # print(globals())
    # delete_s("s")
    # print(globals())
    # print(company(company_dict))
    # print(list_and_two_index([12, 14, -3, -20, 45], -1, 10))
    # print(work_list(names, salarys, premiums))
    # print(list_for_sorted)
    # sort_spisok(list_for_sorted)
    # print(list_for_sorted)
    # print(dict_unicod("1 10"))
    print(sorted_unicod("У белой вороны есть сыр"))
