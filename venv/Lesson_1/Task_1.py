
# 1.Решить задачи, которые не успели решить на семинаре:
# a. Написать программу, которая будет выводить в консоль ёлочку заданной высоты
# б. Написать порграмму, которая выодит в консоль таблицу умножения "как на тетрадках"

def herringbone(height):
    print(" "*15,"Елочка")
    m = (2 * height) - 2
    for i in range(height):
        for j in range(m):
            print(end=" ")
        m = m - 1
        for j in range(0, i + 1):
            print("*", end=' ')
        print(" ")

def multiplication_table():
    print(" "*15,"Таблица умножения")
    for i in range(2):
        for k in range(1, 11):
            if i == 0:
                num = 2
            else:
                num = 6
            for j in range(4):
                if k != 10:
                    l =f" {k}"
                else:
                    l = f"{k}"
                if len(str(num * k)) == 1:
                    print(f"{num} * {l} =  {num * k}", end=' ' * 4)
                else:
                    print(f"{num} * {l} = {num * k}", end=' '* 4)
                num +=1
            print()
        print()



if __name__ == '__main__':
    herringbone(10)
    print()
    multiplication_table()