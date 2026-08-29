from functools import wraps
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
        Декоратор, который задаёт вопрос пользователю перед вызовом декорируемой функции.
        Args:
            func: Функция, которую нужно декорировать.
        Returns: Ссылка на функцию-обёртку.
    """
    @wraps(func)
    def wrapper(*args,**kwargs)->Any:
        """
            Обёртка для декорируемой функции, осуществляющая взаимодействие с пользователем.
            Args:
            *args: Позиционные аргументы, передаваемые в декорируемую функцию.
             **kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
            Returns: Результат, возвращаемый декорируемой функцией.
        """
        res = input("как дела? ")
        print(f"У тебя {res}, а у меня не очень! Ладно, держи свою функцию.")
        res = func(*args,**kwargs)
        return res
    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')
test()