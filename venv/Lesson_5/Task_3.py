# ✔Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib(num: int):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b




if __name__ == '__main__':
    print(*(fib(10)))
