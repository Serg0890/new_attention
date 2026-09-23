import time
from typing import Callable, Any


def timer(func: Callable) -> Any:
    def wrapper(*args,**kwargs):

        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        run_time = end - start
        print(f"функция {func.__name__} работала: {round(run_time, 4)} sec")
        return res
    return wrapper


def logging(func: Callable) -> Callable:
    """декоратор логирующий функцию"""

    def wrapper(*args, **kwargs) -> Any:
        print(f"вызывается функция {func.__name__}\n"
              f"позиционные аргументы {args}\n"
              f"именованные аргументы {kwargs}")
        res = func(*args, **kwargs)
        print(f"функция завершила работу")
        return res
    return wrapper


@logging
@timer
def square_sum() -> int:
    number = 100
    res = 0
    for _ in range(number + 1):
        res += sum([i_num ** 2 for i_num in range(10000)])
    return res

@timer
@logging
def cube_sum(number) -> int:
    number = 100
    res = 0
    for _ in range(number + 1):
        res += sum([i_num ** 3 for i_num in range(10000)])
    return res


my_sum = square_sum()
print(my_sum)

print("\n")
my_cubes = cube_sum(200)
print(my_cubes)