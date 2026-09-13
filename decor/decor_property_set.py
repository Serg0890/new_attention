class Person:
    """
    Человек

    Args:
        name (str): имя
        age (int): возраст

    Attributes:
        _name(str): имя
        _age(int): возраст (от 1 до 100, иначе ошибка)
    """

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.age = age

    def __str__(self) -> str:
        return "Имя: {name} \tВозраст: {age}".format(name=self._name, age=self._age)

    @property
    def age(self) -> int:
        """Геттер. Возвращает возраст"""
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        """
        Сеттер.
        Устанавливает возраст в диапазоне от 1 до 100,
        иначе выбрасывает исключение
        """
        if age in range(1, 100):
            self._age = age
        else:
            raise Exception("Недопустимый возраст")

    @property
    def name(self) -> str:
        """Геттер. Возвращает имя"""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Сеттер. Устанавливает имя"""
        self._name = name


tom = Person("tom", 1)

print(tom)
tom._age = 10
print(tom)
