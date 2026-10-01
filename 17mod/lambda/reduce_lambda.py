from functools import reduce
from typing import List


def my_add(a: int, b: int) -> int:
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


def my_sap(a: int, b: int):
    res = a * b
    print(f"{a} * {b} = {res}")
    return res


numbers: List[int] = [4, 1, 2, 3, 4]
# print(reduce(my_add, numbers))
# print(reduce(my_sap, numbers))

sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"]


def count_word(a, b):
    if isinstance(a, str):
        a = a.count("was")
    res = a + b.count("was")

    return res


# print(reduce(count_word, sentences))

sum_count = sum(s.count("was") for s in sentences)
print(sum_count)