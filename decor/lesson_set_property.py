from os import name


class Person:

    def __init__(self, age:int, name:str):
        self._age = age
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if age in range(18, 100):
            self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name


tom = Person(25,"tom")
# print(tom.__class__)
print(tom.age)
tom.age = 30
print(tom.age)
tom.name = "Alex"
print(tom.name)
tom.name = "Mike"
print(tom.name)

