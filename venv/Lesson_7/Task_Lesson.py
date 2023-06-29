import os.path
import random as rnd
from string import ascii_letters
from pathlib import Path


def pair_of_nums(file_name: str, count: int):
    '''
    Задание №1

    Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
    Первое число int, второе - float разделены вертикальной чертой.
    Минимальное число - -1000, максимальное - +1000.
    Количество строк и имя файла передаются как аргументы функции.
    '''
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(count):
            int_num = rnd.randint(-1000, 1001)
            float_num =round(rnd.uniform(-1000, 1001),5)
            f.write(f'{int_num:>5} | {float_num:>5}\n')

def aliases():
    '''
    Задание №2
    
    Напишите функцию, которая генерирует псевдоимена.
    Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
    Полученные имена сохраните в файл.
    '''

    name_lenght = rnd.randint(4, 7)
    vowels = "аоуыэеёиюя"
    letters ='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    name = []
    for i in range(name_lenght // 2):
        name.append(rnd.choice(letters[:9]))
    for i in range(name_lenght // 2 + 1, name_lenght):
        name.append(rnd.choice(letters[10:]))
    rnd.shuffle(name)
    return ''.join(name).title()

def write_name(file_name: str, count: int):
    #Задание №2

    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(count):
            f.write(f'{aliases()}\n')

def task_3(new_file: str):
    '''
    Задание №3

    Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
    Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
    если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
    В результирующем файле должно быть столько же строк, сколько в более длинном файле.
    При достижении конца более короткого файла, возвращайтесь в его начало.
    '''

    massive_nums = []
    massive_name = []
    len_f1 = 0
    len_f2 = 0

    with (
        open('test.txt', 'r', encoding='utf-8') as f1,
        open('name.txt', 'r', encoding='utf-8') as f2,
        open(new_file, 'a', encoding='utf-8') as f3
    ):
        while num := f1.readline():
            int_num, float_num = num.split('|')
            massive_nums.append(int(int_num) * float(float_num))
            len_f1 += 1
        while name := f2.readline():
            massive_name.append(name.replace('\n',''))
            len_f2 += 1

        if len_f1 > len_f2:
            a = len_f1 - len_f2
            for i in range(a):
                massive_name.append(massive_name[i])
        elif len_f1 < len_f2:
            a = len_f2 - len_f1
            for i in range(a):
                massive_nums.append(massive_nums[i])

        for i in range(len(massive_nums)):
            if massive_nums[i] < 0:
                f3.write(f'{massive_name[i].lower()} | {abs(massive_nums[i])}\n')
            elif massive_nums[i] > 0:
                f3.write(f'{massive_name[i].upper()} | {round(massive_nums[i])}\n')
            else:
                f3.write(f'{massive_name[i]} | {massive_nums[i]}\n')

def file_extension(extension: list[str],dir: str, min_name=6, max_name=30, min_bite=256, max_bite=4096, count_file=42):
    '''
    Задание №4

    Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
        ✔ расширение
        ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
        ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
        ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
        ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
        ✔ количество файлов, по умолчанию 42
        ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

    Задание №6

    ✔ Дорабатываем функции из предыдущих задач.
    ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
    ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
    ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
    '''

    for _ in range(count_file):
        ext = random_extension(extension)
        file_size = rnd.randint(min_name, max_name)
        file_name = "".join(rnd.sample(ascii_letters, file_size)) + '.' + ext
        # file_name = 'asdf.txt'
        if not os.path.exists(dir):
            os.mkdir(dir)
        full_name = Path.cwd()/dir/file_name
        if not os.path.exists(full_name):
            # full_name = Path.cwd() / dir / (file_name.split('.')[0] + "_1" + '.' + ext)
            with open(full_name, 'ab') as f:
                size = rnd.randint(min_bite, max_bite)
                result = rnd.randbytes(size)
                f.write(result)

def random_extension(list_ex: list[str]) -> str:
    '''
    Задание №5

    Доработаем предыдущую задачу.
        ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
        ✔ Расширения и количество файлов функция принимает в качестве параметров.
        ✔ Количество переданных расширений может быть любым.
        ✔ Количество файлов для каждого расширения различно.
        ✔ Внутри используйте вызов функции из прошлой задачи.
    '''
    return rnd.choice(list_ex)

def sort_file(path: str):
    '''
    Задание №7

    ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
    ✔ Каждая группа включает файлы с несколькими расширениями.
    ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки
    '''
    for folder in ['video', 'image', 'music', 'docs']:
        # if not os.path.exists(folder):
        #     os.mkdir(folder)
        if not Path(folder).exists():
            Path(folder).mkdir()

    for file in os.listdir(path):
        ext = file.split('.')[1]
        if ext in ['txt', 'md', 'doc']:
            # os.replace(file, os.path.join(os.getcwd(),'docs', file))
            Path(path,file).replace(Path.cwd() / 'docs' / file)
        elif ext in ['png', 'jpg', 'bmp', 'psd']:
            # os.replace(file, os.path.join(os.getcwd(),'docs', file))
            Path(path, file).replace(Path.cwd() / 'image' / file)
        elif ext in ['mp3', 'wav', 'ogg']:
            # os.replace(file, os.path.join(os.getcwd(),'docs', file))
            Path(path, file).replace(Path.cwd() / 'music' / file)
        elif ext in ['mov', 'mp4', 'mkv', 'avi']:
            # os.replace(file, os.path.join(os.getcwd(),'docs', file))
            Path(path, file).replace(Path.cwd() / 'video' / file)



if __name__ == '__main__':
    # pair_of_nums('test.txt', 10)
    # write_name('name.txt', 10)
    task_3('task_3.txt')
    file_extension(['txt', 'md', 'doc', 'rtf', 'png', 'bmp', 'mp3', 'ogg', 'wav', 'mp4', 'avi', 'mov'], dir='test', count_file=30)
    # sort_file("/Users/dasa/Documents/geekbrains/Python2.0/venv/Lesson_7/test")


