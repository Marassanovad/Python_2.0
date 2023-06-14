import random
# ✔ Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

# ✔ *Верните все возможные варианты комплектации рюкзака.

def backpack_size(size):
    full_backpack = []
    things = {"Фонарик": 50,
              "Палатка": 500,
              "Топор": 150,
              "Аптечка": 100,
              "Кружка": 80,
              "Тарелка": 80,
              "Спальник": 300,
              "Спички" : 10}
    for key in random.sample(list(things.keys()), k=8):
        if things.get(key) <= size:
            size -= things.get(key)
            full_backpack.append(key)

    return f'Список вещей: {full_backpack} \nОсталось места: {size}'




if __name__ == '__main__':
    print(backpack_size(600))
    print(backpack_size(300))
    print(backpack_size(200))