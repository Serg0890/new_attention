def two_call(func):
    def wraps(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wraps



def greeting(name):
    print(f'Привет, {name}!')



greeting = two_call(greeting)
greeting("!")






