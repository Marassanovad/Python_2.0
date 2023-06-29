import csv
import json
import pickle
import os


def recreate_file_to_json(file_name: str):
    '''
    # Задание №1

    # 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
    # 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
    # 📌 Имена пишите с большой буквы.
    # 📌 Каждую пару сохраняйте с новой строки.
    '''
    my_dict = {}

    with(
        open(file_name, 'r', encoding='utf-8') as read_file,
        open('json_file.json', 'a', encoding='utf-8') as writer_file
    ):
        while data := read_file.readline():
            name, num = data.replace('\n', '').split('|')
            my_dict[str(name).title()] = float(num)
        json.dump(my_dict, writer_file, ensure_ascii=False, separators=(',\n', ':'))

def user_input():
    user_list = []
    while True:
        name = input("Введите имя: ")
        if not name:
            return user_list
        while True:
            id_ = input("Введите личный идентификатор: ")
            if id_.isdigit() and not id_ in [uid[2] for uid in user_list]:
                break
        while True:
            access_level = input("Введите уровень доступа: ")
            if access_level.isdigit() and 0 < int(access_level) < 8:
                user_list.append((name, access_level, id_))
                break

def unlimited_while(name_file: str):
    '''
    Задание №2

    📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
    📌 После каждого ввода добавляйте новую информацию в JSON файл.
    📌 Пользователи группируются по уровню доступа.
    📌 Идентификатор пользователя выступает ключём для имени.
    📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
    📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
    '''
    user_list = user_input()
    result_dict = {}
    for user in user_list:
        if user[1] in result_dict:
            result_dict[user[1]].update({user[2]: user[0]})
        else:
            result_dict[user[1]] = {user[2]: user[0]}
    with open(name_file, 'a+', encoding='utf-8') as writer_file:
        # my_dict = {access_level: {id_: name.title()}}
        json.dump(result_dict, writer_file, indent=4, ensure_ascii=False)

def save_task_2_as_csv(name_file: str):
    '''
    Задание №3

    Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
    '''
    with (open(name_file, 'r', encoding='utf-8') as read_file,
          open("task_3.csv", 'w', encoding='utf-8') as write_file):
        json_read = json.load(read_file)
        csv_write = csv.writer(write_file, dialect='excel', quoting=csv.QUOTE_ALL)
        # fieldnames = ["access level", 'id', 'name'],
        # csv_write.writeheader()
        csv_write.writerow(["access level", 'id', 'name'])
        for access_level, value in json_read.items():
            all_data = []
            for id_, name in value.items():
                all_data.append((access_level, name, id_))
            csv_write.writerows(all_data)
            # csv_write.writerows(user[1])

def create_csv_file(name_file: str, new_file='task_4.json'):
    '''
    Задание №4

    📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
    📌 Дополните id до 10 цифр незначащими нулями.
    📌 В именах первую букву сделайте прописной.
    📌 Добавьте поле хеш на основе имени и идентификатора.
    📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
    📌 Имя исходного и конечного файлов передавайте как аргументы функции.
    '''

    with (open(name_file, 'r', encoding='utf-8') as read_file,
          open(new_file, 'w', encoding='utf-8') as write_file):
        spamreader = csv.reader(read_file, dialect='excel')
        new_dict = {}
        next(spamreader)
        for row in spamreader:
            uid = f'{row[2]:0>10}'
            name = row[1].title()
            lvl = row[0]
            key = hash(uid + name)
            new_dict[key] = [lvl, name, uid]
        json.dump(new_dict, write_file, ensure_ascii=False, indent=4)

def pickle_search_json(path):
    '''
    Задание №5

    Напишите функцию, которая ищет json файлы в указанной директории и
    сохраняет их содержимое в виде одноимённых pickle файлов.
    '''
    for file in (os.listdir()):
        if os.path.isfile(file):
            init_name, init_ext = os.path.join(file).split('.')
            if init_ext == 'json':
                with open(file, 'r', encoding='utf-8') as file:
                    new_dict = json.load(file)
                    with open((init_name + '.' + 'pickle'), 'wb') as file:
                        pickle.dump(new_dict, file)

def pickle_to_csv(file_pickle):
    '''
    Задание №6

    📌 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
    📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
    📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
    '''

    with(
        open(file_pickle, 'rb') as read_pickle,
        open("csv_file.csv", 'w', encoding='utf-8') as write_csv
    ):
        new_dict = pickle.load(read_pickle)
        csv_w = csv.DictWriter(write_csv, fieldnames=[value for value in new_dict[0]], dialect='excel', quoting=csv.QUOTE_ALL)
        csv_w.writeheader()
        all_data = []
        for value in new_dict:
            all_data.append(value)
        # all_data.append(new_dict)
        # print(all_data)
        csv_w.writerows(all_data)

def read_file_as_pickle(file: str):
    '''
    Задание №7

    📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
    📌 Распечатайте его как pickle строку.
    '''
    with open(file, 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.reader(f)
        for line in csv_file:
            line = pickle.dumps(line)
            print(line)







if __name__ == '__main__':
    # recreate_file_to_json('task_3.txt')
    # unlimited_while('task_2.json')
    # save_task_2_as_csv('task_2.json')
    create_csv_file('task_3.csv')
    # path = os.path.join(os.getcwd())
    # pickle_search_json(path)
    # pickle_to_csv('json_file.pickle') # dont work
    # read_file_as_pickle('csv_file.csv')
