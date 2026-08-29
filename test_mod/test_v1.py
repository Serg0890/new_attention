def is_palindrome(num_list):
    rev_list = num_list[::-1]
    if num_list == rev_list:
        return True
    else:
        return False


nums = [x for x in range(5)]
answer = []

for i_nums in range(0, len(nums)):
    if is_palindrome(nums[i_nums:len(nums)]):
        answer = nums[: i_nums]
        answer.reverse()
        break

print("исходный список", nums)
print("Нужно чисел для полиндрома", len(answer))
print("список этих чисел", answer)
