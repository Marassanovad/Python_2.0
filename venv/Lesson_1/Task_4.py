# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

def lucky_game():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    COUNT_TRY = 10
    RAND_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
    is_win = True
    for _ in range(COUNT_TRY):
        num = int(input("Введите число от 0 до 1000: "))
        if num > RAND_NUMBER:
            print("Ваше число БОЛЬШЕ загаданного")
            is_win = False
        elif num < RAND_NUMBER:
            print("Ваше число МЕНЬШЕ загаданного")
            is_win = False
        else:
            print("Вы выиграли!!!")
            is_win = True
    if not is_win == True:
        print("Вы проиграли")


if __name__ == '__main__':
    lucky_game()