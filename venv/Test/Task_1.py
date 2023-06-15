
def data_types():
    a = input("Введите текст: ")
    print(a , type(a), id(a),hash(a), sep = '\n')

def simple_object():
    text = input("Введите текст: ")
    if text.isdigit():
        print(bin(int(text)))
        print(oct(int(text)))
        print(hex(int(text)))
    else:
        if text.isascii():
            print("Текст содержит кодировку ASSCII")
        else:
            print("текст нне содержит кодировку ASSCII")



if __name__ == '__main__':
    data_types()  # задания 1
    # help() # задания 2 - keywords, задания 3 - symbols
    # simple_object() # задания 3

    # Лекция №4
    # data = [25, -42, 146, 73, -100, 12]
    # print(list(map(str, data)))
    # print(max(data, key=lambda x: -x))
    # print(*filter(lambda x: not x[0].startswith('__'), globals().items()))


