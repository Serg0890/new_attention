from functools import wraps
from typing import Callable


def cache_decor(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(number: int) -> int:
        if number not in cache:
            cache[number] = func(number)
        return cache[number]

    wrapper.get_cache = lambda: cache
    return wrapper


@cache_decor
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования

print(fibonacci(5))  # Результат будет кеширован
print(fibonacci.get_cache())
# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

print(fibonacci.get_cache())
# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
