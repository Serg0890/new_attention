from dataclasses import replace

string_inp = 'гвозди:шурупы:гайки'
words_list = list(string_inp)

print(words_list)
repl = ':'
res_repl = ';'
index = 0
replace_count = 0

for index, value in enumerate(words_list):
    if value == repl:
        words_list[index] = res_repl
        replace_count += 1
    index += 1

for letter in words_list:
    print(letter, end='')

print(f'\nзамен {replace_count}')
count_in_list = int(input("количество чисел в списке "))
numbers_list = []

for i in range(count_in_list):
    number = int(input(f"введите {i + 1} число "))
    numbers_list.append(number)

delitel = int(input("введите делитель "))

for i, v in enumerate(numbers_list):
    if v %  delitel == 0:
        print(f"индекс числа {v} = {i}")

