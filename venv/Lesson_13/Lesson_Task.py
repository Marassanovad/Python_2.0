'''
Задание No1
📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
📌 Обрабатывайте не числовые данные как исключения.

 Задание No2
📌 Создайте функцию аналог get для словаря.
📌 Помимо самого словаря функция принимает ключ и
значение по умолчанию.
📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
📌 Реализуйте работу через обработку исключений.

 Задание No3
📌 Создайте класс с базовым исключением и дочерние классы- исключения:
○ ошибка уровня,
○ ошибка доступа.

 Задание No4
📌 Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

 Задание No5
📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
📌 загрузка данных (функция из задания 4)
📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

 Задание No6
📌 Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
📌 Передавайте необходимые данные из основного кода проекта.
'''

def number():
    while True:
        try:
            num = int(input('Введите число: '))
            if '.' in num:
                return float(num)
            return int(num)
        except ValueError as e:
            print(f'Ошибка: {e}')


def get_dict(dict_work: dict, default_value):
    try:
        return dict_work[key]
    except Exception:
        return default_value


class ErrorDefault(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)

    def __str__(self):
        return 'Я родился'

class ErrorLevel(ErrorDefault):
    def __init__(self, *args: object):
        super().__init__(*args)

    def __str__(self, string: str = '') -> str:
        return 'Error level' + string

class ErrorAccess(ErrorLevel):
    def __str__(self, string: str = '') -> str:
        return 'Error Access' + string

class User:

    def __init__(self, name, id, access_lvl):
        self.name = name
        self.id = id
        self.access_lvl = access_lvl

    def user_input(self):
        user_list = []
        
        while True:
            name = input("Введите имя: ")
            if not name:
                return User(*user_list)
            while True:
                id_ = input("Введите личный идентификатор: ")
                if id_.isdigit() and not id_ in [uid[2] for uid in user_list]:
                    break
            while True:
                access_level = input("Введите уровень доступа: ")
                if access_level.isdigit() and 0 < int(access_level) < 8:
                    user_list.append((name, access_level, id_))
                    break

    def recreate_file_to_json(self, file_name: str):

        my_dict = {}

        with(
            open(file_name, 'r', encoding='utf-8') as read_file,
            open('json_file.json', 'a', encoding='utf-8') as writer_file
        ):
            while data := read_file.readline():
                name, num = data.replace('\n', '').split('|')
                my_dict[str(name).title()] = float(num)
            json.dump(my_dict, writer_file, ensure_ascii=False, separators=(',\n', ':'))


if __name__ == '__main__':
    number()