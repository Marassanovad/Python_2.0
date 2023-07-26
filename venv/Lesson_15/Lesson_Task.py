import os
import random
import logging
import sys
from datetime import datetime
from calendar import monthrange
from collections import namedtuple

'''
 Задание No1
📌 Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.

 Задание No2
📌 На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
📌 Напишите аналогичный декоратор, но внутри используйте модуль logging.

 Задание No3
📌 Доработаем задачу 2.
📌 Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.

 Задание No4
📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3- я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответсвует формату.

 Задание No5
📌 Дорабатываем задачу 4.
📌 Добавьте возможность запуска из командной строки.
📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
📌 *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые,
т.е не мая, а 5.

 Задание No6
📌 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
📌 Соберите информацию о содержимом в виде объектов namedtuple.
📌 Каждый объект хранит:
        ○ имя файла без расширения или название каталога,
        ○ расширение, если это файл,
        ○ флаг каталога,
        ○ название родительского каталога.
📌 В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

def task_1():
    num = int(input('Enter num'))
    if num == 0:
        logging.basicConfig(filename='task_1_log.log', filemode='a', encoding='utf-8', level=logging.INFO)
        logging.info('ZeroDivivsionError: division by zero')
    for_num = random.randint(1, 100) / num
    return for_num



def directory_info(path=os.getcwd()):
    info = os.listdir(path)
    Info = namedtuple("Info", ['name', 'extension', 'catalog_flag', 'parent_directory'])
    print(info)
    logging.basicConfig(filename='DIRECTORY_INFO.log.', filemode='a', encoding='utf-8', level=logging.INFO)
    for i in info:
        i = os.path.join(path, i)
        if os.path.isfile(i):
            new_info_ob = Info(*i.split('/')[-1].split("."), False, path)
            logging.info(new_info_ob)

        if os.path.isdir(i):
            new_info_ob = Info(i.split('/')[-1], None, True, path)
            logging.info(new_info_ob)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        directory_info(sys.argv[1])
    else:
        directory_info()






