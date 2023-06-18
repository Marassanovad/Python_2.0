# ✔Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.

def absolute_path(path: str):
    *path_file, file = path.split('/')
    path_file = "/".join(path_file)
    name_file, file_extension = file.split(".")
    path_turple = (path_file, name_file, file_extension)
    return  path_turple


if __name__ == '__main__':
    path = '/Users/dasa/Documents/geekbrains/Python2.0/venv/Lesson_1/Task_2.py'
    print(absolute_path(path))