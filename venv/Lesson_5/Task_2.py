#Напишите однострочный генератор словаря, который принимает на вход три
#списка одинаковой длины:
#   имена str,
#   ставка int,
#   премия str с указанием процентов вида «10.25%».
#В результате получаем словарь с именем в качестве ключа
#и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная
#на процент премии



def premium(names: list[str], salarys: list[int], premiums: list[str]):
    if len(names) == len(salarys) == len(premiums):
        dict_result = {name: round(salary / 100 * float(premium.replace("%", ""))) for name, salary, premium in zip(names, salarys, premiums)}
        return dict_result
    else:
        return False






if __name__ == '__main__':
    names = ("Sasha", "Dasha", "Masha")
    salarys = (12000, 12000, 12000)
    premiums = ("10.23%", "11%", "12%")

    #генератор в одну строку
    #print({name: round(salary / 100 * float(premium.replace("%", ""))) for name, salary, premium in zip(names, salarys, premiums)})

    #тоже генератор в одну строку, но в методе
    print(premium(names, salarys, premiums))