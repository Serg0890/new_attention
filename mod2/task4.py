nums_list = []
N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)
maximum = nums_list[0]
minimum = nums_list[0]
for i in nums_list:
    if maximum < i:
        maximum = nums_list[i]
    if minimum > i:
        minimum = nums_list[i]
print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)
