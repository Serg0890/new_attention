from typing import Callable

count_global = 0


def counter(func: Callable) -> Callable:
    """счаетичик вызова"""
    count_local = 0

    def wrapped(*args, **kwargs):
        nonlocal count_local
        count_local += 1
        global count_global
        count_global +=1
        print(f"функция {func.__name__} была вызвана через глобальный счетчик {count_global} раз")
        print(f"функция {func.__name__} была вызвана через локальный счетчик {count_local} раз")
        return func(*args,**kwargs)
    return wrapped

@counter
def hello() -> None:
    print("hello")

@counter
def hello_2() -> None:
    print("hello2")


hello()
hello()
hello_2()
hello_2()
