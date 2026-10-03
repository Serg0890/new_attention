from typing import List

# numbers = input("введите числа ")
# print(sorted(list(map(int, numbers.split(" ")))))


my_string = "qWe456rtY"

# print(list(filter(lambda x: not (x.isupper() or x.isdigit()), my_string)))

num1: List[int] = [1, 2, 3, 4, 5]
num2: List[int] = [12, 6, 7, 9, 9]
result: List[int] = list(map(lambda x, y: x + y, num1, num2))

# print(result)

res_even: List[int] = list(filter(lambda x: x % 2 != 0, result))
# print(res_even)

res = map(lambda num: num * 5, filter(lambda x: x % 2, num1))
print(list(res))
