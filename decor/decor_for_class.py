import time

from typing import Callable
from datetime import datetime, UTC
import functools
from functools import wraps


def create_time(cls):
    """декор класса"""

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print("время создания инст класса", datetime.now())
        return instance

    return wrapper


def timer(func: Callable) -> Callable:
    """выводит время работы функции"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("время работы функции: ", end - start)
        return res

    return wrapper


def decor_all_method(decorator: Callable) -> Callable:
    """декоратор класса"""

    @wraps(decorator)
    def decorate(cls):
        for i_met_name in dir(cls):
            if i_met_name.startswith("__") is False:
                cur_met = getattr(cls, i_met_name)
                decor_met = decorator(cur_met)
                setattr(cls, i_met_name, decor_met)
        return cls
    return decorate


@create_time
@decor_all_method(timer)
class Functions:

    def __init__(self, max_num: int) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        res = 0
        for _ in range(number + 1):
            res += sum([i_num ** 2 for i_num in range(self.max_num)])

        return res

    def cube_sum(self, number: int) -> int:
        res = 0
        for _ in range(number):
            res += sum([i_num ** 3 for i_num in range(self.max_num)])
        return res


my_func1 = Functions(max_num=1000)
# time.sleep(1)
# my_func2 = Functions(max_num=2000)
# time.sleep(1)
# my_func3 = Functions(max_num=3000)
my_func1.squares_sum()
my_func1.cube_sum(number=2000)
