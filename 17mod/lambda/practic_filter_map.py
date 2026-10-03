
# numbers = input("введите числа ")
# print(sorted(map(int,(numbers.split()))))

user_string = "qWe456rtY"

res_filter = filter(lambda x: not (x.isupper() or x.isdigit()), user_string)
print(list(res_filter))
