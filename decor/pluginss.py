from typing import Callable

PLUGIN = dict()


def register(func: Callable) -> Callable:
    """декоратор регистрирует функцию как плагин"""
    PLUGIN[func.__name__] = func
    return func

@register
def say_hello(name: str) -> str:
    return f"hello {name}"

@register
def say_goodbye(name: str) -> str:
    return f"goodbye {name}"


print(PLUGIN)
print(say_hello("tom"))
print(say_goodbye("alex"))