import functools


def repiat(num_times):
    print(f"фаюрика вызвана {num_times} вернет декоратор")

    def decor_repiat(func):
        print(f"декор создан обернет фун {func.__name__}")

        @functools.wraps(func)
        def wraps(*args, **kwargs):
            print(f"обертка вызвана поавторяем {num_times} раз")

            last_res = None

            for _ in range(num_times):
                last_res = func(*args, **kwargs)
            return last_res  # верну рез посл вызова

        return wraps #декор возвр обертку
    return decor_repiat # фабрика возвр декоратор

@repiat(num_times=4)
def foo(name):
    print(f"privet {name}")


foo("serg")

