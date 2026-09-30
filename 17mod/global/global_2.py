from typing import Callable
import builtins

count_global = {}


def counter(func: Callable) -> Callable:
    """счаетичик вызова"""
    count_local = {}

    def wrapped(*args, **kwargs):
        nonlocal count_local
        global count_global
        count_global[func.__name__] = count_global.get(func.__name__, 0) + 1
        count_local[func.__name__] = count_local.get(func.__name__, 0) + 1
        print(f"локально вызвана {count_local}, глобально вызвана {count_global}")
        return func(*args, **kwargs)

    wrapped.check_count = count_local
    return wrapped

check_gl_count = count_global

@counter
def hello() -> None:
    print("hello")


@counter
def hello_2() -> None:
    print("hello")


hello()
hello()
hello_2()
hello_2()

# print(check_gl_count)
# print(hello_2.check_count)
# print(hello.check_count)
# print("*" * 100)
# print(dir(__builtins__))
print(dir(builtins))

print(dir(43))