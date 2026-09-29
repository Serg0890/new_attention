def f1():
    print(f"num = {number}")

def f2():
    number = 50
    print(f"num in f2 = {number}")

def f3():
    def f4():
        # nonlocal number
        global number
        number = 10
        print(f"in f3/f4 {number}")

    number = 30
    print(f"in f3 num = {number}")
    f4()
    print(f"in f3 num = {number}")


number = 100
print(f"global num = {number}")
f1()
f2()
f3()
f1()
print(f"global num = {number}")

