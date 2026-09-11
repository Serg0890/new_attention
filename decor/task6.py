from time import sleep
from typing import Callable, Any
from functools import wraps


def slowdown_2(func: Callable) -> Callable:
    """
    декоратор замедляект на 2 сек
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Обёртка для декорируемой функции, осуществляющая задержку перед вызовом.
        Задерживает выполнение на 2 секунды, а затем вызывает оригинальную функцию
        с переданными ей аргументами.
        Args:
            *args: Позиционные аргументы, передаваемые в декорируемую функцию.
            **kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
        Returns: Результат, возвращаемый декорируемой функцией.
        """
        print("start slow")
        sleep(2)

        res = func(*args, **kwargs)
        # print("okeeeyy")
        return res

    return wrapper

@slowdown_2
def say_hello(name):
    print(f"привет {name}")


print(slowdown_2.__doc__)