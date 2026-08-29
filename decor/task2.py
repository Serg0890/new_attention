import time
from collections.abc import Callable
from curses import wrapper
from typing import Any


def timer(func: Callable)->Callable:

    """
    Деоратор выводящий время функции
    """
    def wrapper_timer(*args, **kwargs)->Any:
        start_at = time.time()
        result = func(*args,**kwargs)
        stop_at= time.time()
        run_time = round(stop_at - start_at, 4)
        print("функция работала {} секунд".format(run_time))
        return result
    return wrapper_timer

