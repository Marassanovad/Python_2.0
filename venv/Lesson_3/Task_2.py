# ✔ Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

def dublicate_list():
    my_list = [1, 2, 3, 4, 4, 5, 5, 6, 6, 6]
    new_list = []

    for el in my_list:
        if my_list.count(el) > 1 and el not in new_list:
            new_list.append(el)
    return new_list


if __name__ == '__main__':
    print(dublicate_list())