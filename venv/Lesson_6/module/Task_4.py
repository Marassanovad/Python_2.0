import sys

#Задание №7

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


def _leap_year(year: int):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

def my_date(date: str):
    day, month, year =list(map(int, date.split('.')))
    if 1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999:
        if month in [4, 6, 9, 11] and day < 31:
            return True
        elif month in [1,3, 5, 7, 8, 12] and day <= 31:
            return True
        elif _leap_year(year) and day <= 29:
            return True
        elif not _leap_year(year) and day <= 28:
            return True
        else:
            return False
    else:
        return False



# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты
# на проверку.

print(my_date(sys.argv[1]))

# print(my_date('25.12.1990'))
# print(my_date('28.2.2023'))
# print(my_date('31.5.1990'))
# print(my_date('32.2.1990'))
