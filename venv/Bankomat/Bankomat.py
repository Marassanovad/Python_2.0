class Bankomat:

    def __init__(self, balance):
        self.balance = balance

    def balance(self):
        return f"Текущий баланс: {self.balance}"


    def top_up(self, sum): # пополнения
        if sum % 50 == 0:
            self.balance = self.balance + sum
            return f"Операция была успешна \n{Bankomat.balance(self)}"
        else:
            return "Сумма пополнения долна быть кратна 50"

    def withdraw(self, sum): # снятия
        if sum % 50 == 0:
            percent = sum * 0.015
            if percent < 30:
                percent = 30
            elif percent > 600:
                percent = 600
            if self.balance < (sum + percent):
                return "На балансе недостаточно средств"
            else:
                self.balance -= (sum + percent)
                return f"Операция была успешна \n{Bankomat.balance(self)}"
        else:
            return "Сумма снятия долна быть кратна 50"


    def percent_for_operation(self): # бонус за использования
        self.balance += (self.balance * 0.03)
        return f"Спасибо за использования нашего БАНКОМАТА \nЗа это мы вам начислем бонусы :) \n" \
               f"{Bankomat.balance(self)}"

    def limit(self): # ха-ха че то вы очень богатый
        if self.balance >= 5_000_000:
            self.balance -= (self.balance * 0.10)
            return "Ой, у вас очень много денег. Поэтому мы немного заберем"

    def menu(self, i): # меню банкомата
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








