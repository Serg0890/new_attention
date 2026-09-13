from datetime import datetime
from functools import wraps
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """
        Декоратор для логирования информации о функции, её документации
        и обработки ошибок при выполнении.
        При каждом вызове декорируемой функции он выводит на экран её название
        и документацию. В случае возникновения исключения информация об ошибке
        записывается в файл `function_errors.log`.
        Args:
            func: Функция, которую нужно декорировать.
        Returns: Ссылка на функцию-обёртку.
        """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Обёртка для декорируемой функции, осуществляющая логирование и обработку ошибок.
        Args:
            *args: Позиционные аргументы, передаваемые в декорируемую функцию.
            **kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
        Returns: Результат, возвращаемый декорируемой функцией.
        """

        try:
            print(f'Название функции: {func.__name__}')
            print(f'Документация функции: {func.__doc__}')
            result = func(*args, **kwargs)
            return result
        except Exception as err:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                print(f'Ошибка при вызове функции {func.__name__}')
                file.write(
                    f'Функция: {func.__name__}, ошибка: {err}, время возникновения ошибки: {datetime.now()}\n')

    return wrapper


@logging
def sum_my(a, b):
    """

    :param a: число int
    :param b: число Int
    :return: сложение
    """
    res = a + b
    return res


print(sum_my("v", 4))
