
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
def herringbone_2(height):
    for i in range(height):
        print(f'{"*"*(i*2+1):^{height*2+1}}')
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
def multiplication_table_2():
    for x in range(2, 11):
        for y in range(2, 6):
            print(f'{y:^3} X {x:^3} = {x*y:^3}\t\t\t', end='')
        print()
    print()
    for x in range(2, 11):
        for y in range(6, 10):
            print(f'{x:^3} X {y:^3} = {x*y:^3}\t\t\t', end='')
        print()

if __name__ == '__main__':
    herringbone(10)
    print()
    herringbone_2(10)
    print()
    multiplication_table()
    print()
    multiplication_table_2()