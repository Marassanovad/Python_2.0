#Задание №8

# Создайте пакет с всеми модулями, которые вы создали за время занятия.
# Добавьте в __init__ пакета имена модулей внутри дандер __all__.
# В модулях создайте дандер __all__ и укажите только те функции, которые
# могут верно работать за пределами модуля.

from .Task_2 import lucky_game
from .Task_3 import mystery, puzzles, number_of_guesses, result_
from .Task_4 import my_date

__all__ = ['lucky_game', 'mystery', 'puzzles', 'number_of_guesses', 'result_', 'my_date']