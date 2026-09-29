from functools import wraps
from typing import Callable

count_glob = 0


def counter_dec(func: Callable) -> Callable:
    """Декоратор, считающий ивыводящий количество вызовов декорируемой функции."""
    count_local = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count_local
        count_local += 1

        global count_glob
        count_glob += 1
        print(f"func {func.__name__} вызывается через global count {count_glob} раз")
        print(f"func {func.__name__} вызывается через local count {count_local} раз")
        return func(*args, *kwargs)

    return wrapper


@counter_dec
def hello() -> None:
    print("hello ")


@counter_dec
def hello_2():
    print("hello")


hello()
hello()
hello_2()
hello_2()
