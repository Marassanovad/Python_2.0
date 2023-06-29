import json
import csv
import pickle
import os

# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
#   ○ Для дочерних объектов указывайте родительскую директорию.
#   ○ Для каждого объекта укажите файл это или директория.
#   ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

def recursively_bypasses(dir: str):
    size_dirs = 0
    my_dict = {}
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        item_dict = {'parent': path.split("/")[-2], 'type': None, 'size': None}
        my_dict[path.split("/")[-1]] = item_dict
        if os.path.isfile(path):
            item_dict['type'] = 'file'
            item_dict['size'] = f"{os.path.getsize(path)} bytes"
        elif os.path.isdir(path):
            size_dirs += os.path.getsize(path)
            item_dict['type'] = 'folder'
            item_dict['size'] = f"{size_dirs} bytes"
            my_dict.update(recursively_bypasses(path))
    return my_dict



def save_result_json(my_dict: dict):
    with open("dir_json.json", 'w', encoding='utf-8') as write_file:
        json.dump(my_dict, write_file, ensure_ascii=False, indent=4)

def save_result_csv(my_dict: dict):
    with open("dir_csv.csv", 'w', encoding='utf-8', newline='') as write_file:
        writer = csv.writer(write_file, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer.writerow(('name', 'parent', 'type', 'size'))
        for k, v in my_dict.items():
            writer.writerow((k, v['parent'], v['type'], v['size']))

def save_result_pickle(my_dict: dict):
    with open('dir_pickle.pickle', 'wb') as f:
        pickle.dump(my_dict, f)



if __name__ == '__main__':
    my_dict = recursively_bypasses("/Users/dasa/Documents/geekbrains/Python2.0/venv/Test")
    save_result_json(my_dict)
    save_result_csv(my_dict)
    save_result_pickle(my_dict)

