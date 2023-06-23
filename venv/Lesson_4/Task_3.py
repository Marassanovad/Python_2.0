# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не
# хешируем, используйте его строковое представление.


def idontunderstand(**kwargs):
    my_dict = {}
    for value, key in kwargs.items():
        if isinstance(key, (list, dict, set, bytearray)):
            key = str(key)
        my_dict[key] = value
    return my_dict



if __name__ == '__main__':
    print(idontunderstand(lll="sss", num=123, spisok={1, 2, 3, 4}, skuchno=[1, 2, 3, 4], spisok_2={'1': 12, 2: 10, 3: 11}))