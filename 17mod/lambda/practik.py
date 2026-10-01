from functools import reduce
from pydoc import text
from string.templatelib import convert

words = ["banana", "apple", "cat", "aaa"]

res = sum(x.count("a") for x in words)

data = "1, 2, 3, 4, 5"


# print(sum(map(int, data.split(","))))#решения!!!!!!
# print(list(map(int, data.split(","))))#решения!!!!!!

def count_word(a, b):
    if isinstance(a, str):
        a = a.count("was")
    return a + b.count("was")


sentences = []
# print(reduce(count_word, sentences))#решения!!!!!!

text = "she was here, but wasabi was not was"

"""3 варианта решения одного и тогоже"""
print(text.split().count("was"))
print(sum(1 for x in text.split() if x == "was"))
print(sum(x == "was" for x in text.split()))
# #решения!!!!!!
