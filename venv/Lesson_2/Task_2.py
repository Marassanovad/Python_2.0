# 2. Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def notation(number, system): # Задания 1. Система счисления
    RESULT = ''
    while number >= 1:
        ost = number % system
        if system == 16:
            if ost == 10:
                ost = 'a'
            elif ost == 11:
                ost = 'b'
            elif ost == 12:
                ost = 'c'
            elif ost == 13:
                ost = 'd'
            elif ost == 14:
                ost = 'e'
            elif ost == 15:
                ost = 'f'
        RESULT += str(ost)
        number = number // system
    return RESULT[::-1]


def notation_2(number, system): # Задания 1. Система счисления
    RESULT = ''
    num = number
    BASE_LETTERS = '0123456789ABCDEF'
    while number >= 1:
        RESULT = BASE_LETTERS[number % system] + RESULT
        number //= system

    return f"Число {num} в {system}-системе равно {RESULT}"
if __name__ == '__main__':
    print(notation(1200 , 16), hex(1200))
    print(notation(54000, 16), hex(54000))