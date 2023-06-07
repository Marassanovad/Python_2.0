# 1.Решить задачи, которые не успели решить на семинаре.
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
from typing import Any


class Bankomat:

    def __init__(self, balance):
        self.balance = balance

    def balance(self):
        return f"Текущий баланс: {self.balance}"


    def top_up(self, sum):
        if sum % 50 == 0:
            self.balance = self.balance + sum
            return f"Операция была успешна \n{Bankomat.balance(self)}"
        else:
            return "Сумма пополнения долна быть кратна 50"

    def withdraw(self, sum):
        if sum % 50 == 0:
            percent = sum * 0.015
            if percent < 30:
                percent = 30
            elif percent > 600:
                percent = 600
            if self.balance < (sum + percent):
                return "На балансе не достаточно средств"
            else:
                self.balance -= (sum + percent)
                return f"Операция была успешна \n{Bankomat.balance(self)}"
        else:
            return "Сумма снятия долна быть кратна 50"


    def percent_for_operation(self):
        self.balance += (self.balance * 0.03)
        return f"Спасибо за использования нашего БАНКОМАТА \nЗа это мы вам начислем бонусы :) \n" \
               f"{Bankomat.balance(self)}"

    def limit(self):
        if self.balance >= 5_000_000:
            self.balance -= (self.balance * 0.10)
            return "Ой, у вас очень много денег. Поэтому мы немного заберем"

    def menu(self, i):
        match i:
            case 0:
                print("-"*50)
                print("Выберите операцию")
                print("1.Пополнения")
                print("2.Снятия")
                print("3.Посмотреть баланс")
                print("4.Выйти")
            case 1:
                print(Bankomat.balance(self))
                print("-"*50)
                print(Bankomat.top_up(self, int(input("Введите сумму пополнения: "))))
            case 2:
                print(Bankomat.balance(self))
                print("-" * 50)
                print(Bankomat.withdraw(self, float(input("Введите сумму снятия: "))))
            case 3:
                print(Bankomat.balance(self))
                print()
            case 4:
                print("Спасибо за использования нашего БАНКОМАТА")
            case _:
                print("Ой, что-то пошло не так")








if __name__ == '__main__':
    operation = 0
    bankomat = Bankomat(5_000_000)
    print("Добро пожаловать в наш БАНКОМАТ")
    while True:
        Bankomat.menu(bankomat, 0)
        k = int(input("Введите число: "))
        print(Bankomat.limit(bankomat))
        Bankomat.menu(bankomat, k)
        operation +=1
        if operation % 3 == 0:
            print(Bankomat.percent_for_operation(bankomat))
        if k == 4:
            break



