import logging
import sys
from datetime import datetime
from calendar import monthrange

'''
Первое задание
Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответсвует формату.
📌 Добавьте возможность запуска из командной строки.
📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
📌 Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

'''

logging.basicConfig(filename='date.log', level=logging.ERROR, encoding='utf-8')

def task_date(text: str=''):
    try:
        week, day, month = check_data(text)
        year = datetime.now().year
        days_count = monthrange(year, month)[1]
        week_counter = 0
        for i in range(1, days_count + 1):
            data = datetime(day=i, month=month, year=year)
            if data.weekday() == day:
                week_counter += 1
                if week_counter == week:
                    return data
    except Exception as e:
        logging.error(f'У вас ошибка: {e}')


def check_data(text:str):
    months = {'янв': 1, 'фев': 2, 'мар': 3, "апр": 4, "мая": 5, "июн": 6, "июл": 7, "авг": 8, "сен": 9,
              "окт": 10, "ноя": 11, "дек": 12}
    days = {"понедельник": 0, "вторник": 1, "среда": 2, "четверг": 3, "пятница": 4, "суббота": 5, "воскресенье": 6}
    week = 0
    day = datetime.now().weekday()
    month = datetime.now().month
    try:
        data = text.split()
        for inf in data:
            if inf.isalpha():
                if inf in months:
                    month = months.get(inf[:3], None)
                if inf in days:
                    day = days.get(inf, None)
            else:
                if inf[0].isdigit():
                    week = int(inf[0])
        return week, day, month
    except Exception:
        return Exception

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='time')
    parser.add_argument('-text', metavar='text', type=str, help='enter week', default="3я среда мая")
    # parser.add_argument('-week', metavar='week', type=str, help='enter week', default=1)
    # parser.add_argument('-day', metavar='day', type=str, help='enter day', default=datetime.now().weekday())
    # parser.add_argument('-month', metavar='month', type=str, help='enter month', default=datetime.now().month)

