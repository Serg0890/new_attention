from typing import Callable


def get_some_1(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("some1")
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")

    return wrapper


def get_some_2(func: Callable) -> Callable:
    def wrapper_some_2(*args, **kwargs):
        print("some2")
        print("</----------\\>")
        func(*args, **kwargs)
        print("<\\______/>")

    return wrapper_some_2

@get_some_2
@get_some_1
def sandwich(filler):
    print(filler)

sandwich("мясо")
