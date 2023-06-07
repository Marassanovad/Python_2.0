# 2. Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def notation(number, system): # Задания 1. Система счисления
    RESULT = ''
    while number >= 1:
        OSTATOK = number % system
        if system == 16:
            if OSTATOK == 10:
                OSTATOK = 'a'
            elif OSTATOK == 11:
                OSTATOK = 'b'
            elif OSTATOK == 12:
                OSTATOK = 'c'
            elif OSTATOK == 13:
                OSTATOK = 'd'
            elif OSTATOK == 14:
                OSTATOK = 'e'
            elif OSTATOK == 15:
                OSTATOK = 'f'
        RESULT += str(OSTATOK)
        number = number // system

    return RESULT[::-1]
if __name__ == '__main__':
    print(notation(1200 , 16), hex(1200))
    print(notation(54000, 16), hex(54000))