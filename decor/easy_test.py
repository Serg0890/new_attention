
def decorated(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper


# @decorated
def say_hello():
    print("hello")

say_hello = decorated(say_hello)
say_hello()