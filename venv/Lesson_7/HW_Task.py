import os.path
import random as rnd
from pathlib import Path

# Напишите функцию группового переименования файлов. Она должна:
#   принимать параметр желаемое конечное имя файлов.
#   При переименовании в конце имени добавляется порядковый номер.
#   принимать параметр количество цифр в порядковом номере.
#   принимать параметр расширение исходного файла.
#   Переименование должно работать только для этих файлов внутри каталога.
#   принимать параметр расширение конечного файла.
#   принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#   К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.



def group_rename(count_in_num: int, ext_start: str, ext_finall: str, diapason: list[int], name = '', directory='test'):
    p = Path(Path.cwd(), directory)

    serial_num = '0' * (count_in_num - 1) + '1'
    for file in os.listdir(p):
        if '.' in file:
            file_name, file_ext = file.split('.')
            if file_ext == ext_start:
                Path(p, file).rename(f'{p}/new/{file_name[diapason[0]: diapason[1]]}{name}{serial_num}.{ext_finall}')
                serial_num = '0' * (count_in_num - len(str(int(serial_num)+1))) + str(int(serial_num) + 1)
        else:
            continue

# print(int('99')+1)



group_rename(4, 'txt','txt', [2,8], name='_new_')