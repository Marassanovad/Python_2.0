from string import ascii_lowercase
import doctest
import unittest
import pytest
'''
Задание No1
📌 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
📌 Возвращается строка в нижнем регистре.

 Задание No2
📌 Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

 Задание No3
📌 Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

 Задание No4
📌 Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери
символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

 Задание No5
📌 На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр, площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
📌 Напишите 3-7 тестов unittest для данного класса.

 Задание No6
📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
📌 Напишите 3-7 тестов pytest для данного проекта.
📌 Используйте фикстуры.
'''

def delete_sim(text: str) -> str:
    """
    Удаление всех сиволов кроме латинских букв
    >>> print(delete_sim("kjhgfd"))
    kjhgfd
    >>> print(delete_sim("kjhgfd999"))
    kjhgfd
    >>> print(delete_sim("9 0 9 0"))
    <BLANKLINE>
    >>> print(delete_sim("KJHGfd9 0"))
    kjhgfd
    >>> print(delete_sim("KJHGfd9л0"))
    kjhgfd
    """
    result = ''
    for ch in text.lower():
        if ch in ascii_lowercase + ' ':
            result += ch

    return result

class TestFunc(unittest.TestCase):

    def test1(self):
        self.assertEqual(delete_sim('kjhgf'), 'kjhgf')

    def test2(self):
        self.assertTrue(delete_sim('KJHGF') == 'kjhgf')

    def test3(self):
        self.assertEqual(delete_sim('kjhgf,,'), 'kjhgf')

    def test4(self):
        self.assertEqual(delete_sim('лорgf'), 'gf')

    def test5(self):
        self.assertEqual(delete_sim('лоhGF87,'), 'hgf')


def test_1():
    assert delete_sim('kjhgf') == 'kjhgf', 'Fail'

def test_2():
    assert delete_sim('KJHGF') == 'kjhgf', 'Fail'

def test_3():
    assert delete_sim('kjhgf,,') == 'kjhgf', 'Fail'

def test_4():
    assert delete_sim('лорgf') == 'gf', 'Fail'

def test_5():
    assert delete_sim('лоhGF87,') == 'hgf', 'Fail'


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    # doctest.testmod(verbose=True)
    pytest.main([ '-v'])