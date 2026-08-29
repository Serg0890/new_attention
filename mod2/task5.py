count_in_list = int(input("количество чисел в списке "))
numbers_list = []

for i in range(count_in_list):
    number = int(input(f"введите {i + 1} число "))
    numbers_list.append(number)

delitel = int(input("введите делитель "))

for i, v in enumerate(numbers_list):
    if v %  delitel == 0:
        print(f"индекс числа {v} = {i}")

