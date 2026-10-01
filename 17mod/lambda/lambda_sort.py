from collections import namedtuple


class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, word):
        self._name = word

    @age.setter
    def age(self, val):
        self._age = val




    def __repr__(self) -> str:
        return f"({self.name}, {self.age})"

one = Person("max", 20)
two = Person("alex", 44)
three = Person("bob", 19)

human = [one, two,three]
print(human)

human.sort(key=lambda x: x.name)
print(human)
