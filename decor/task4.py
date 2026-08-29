from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()


def register_plug(func: Callable) -> Callable:
    """декоратор регистрирует функцию как плагин"""
    PLUGINS[func.__name__] = func
    return func


@register_plug
def say_hello(name: str) -> str:
    return f"Hello {name}!"


@register_plug
def say_goodbye(name: str) -> str:
    return f"Goodbye {name}"


print(PLUGINS)
print(say_hello("alex"))
