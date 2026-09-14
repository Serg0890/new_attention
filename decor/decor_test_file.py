import functools
from logging import makeLogRecord
from time import time


def fetch_data_db():
    print("start ")
    time.sleep(2)
    print("отчет готов")


def say_hello(name):
    return f"hello {name}"


greet = say_hello


def apply_function(func, value):
    # Вызываем функцию, которую нам передали
    return func(value)


def double(x):
    return x * 2


result = apply_function(double, 10)


def make_multy(n):
    def multy(x):
        return x * n

    return multy


t1 = make_multy(2)
t2 = make_multy(4)


def simp_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Это внутренняя функция-обертка."""
        print(f"start {func.__name__}")
        res = func(*args, **kwargs)
        print(f"end {func.__name__}")
        return res

    return wrapper


@simp_logger
def say_whee():
    """Простая функция, которая возвращает строку."""
    print("Whee!")
    return "Готово"


@simp_logger
def add(a, b):
    """Умножает два числа и возвращает результат."""
    print("work add")

    res = a + b
    return res


# "Декорируем" нашу функцию вручную
# Передаем say_whee в simple_logger, получаем обратно wrapper
# и записываем его в переменную с тем же именем say_whee.
# wrapped_say_whee = simp_logger(say_whee)

# Теперь `wrapped_say_whee` — это наша "улучшенная" функция
# print("\nВызываем обернутую функцию:")
# result = say_whee()
# print(f"Результат работы: {result}")
#
# print()
# res = add(5,10)
# print(f"Результат работы: {res}")

print(add.__name__)
print(add.__doc__)