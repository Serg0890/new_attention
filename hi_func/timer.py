import time
from typing import Callable, Any


def square_sum() -> int:
    number = 100
    res = 0
    for _ in range(number + 1):
        res += sum([i_num ** 2 for i_num in range(10000)])
    return res

def timer(func: Callable)->Any:
    start = time.time()
    res = func()
    end = time.time()
    run_time = end - start
    print(f"run func = {round(run_time, 4)}")

    return res

res = timer(square_sum)
print(res)


