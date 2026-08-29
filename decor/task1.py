from collections.abc import Callable

def decor(func: Callable):
    def wrapper(*args, **kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper


@decor
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
