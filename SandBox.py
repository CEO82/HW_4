
'''
def change(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


def hello():
    print("Hello")


hello = change(hello)

hello()
hello()

'''

'''change(hello())

hello()'''

def auto_start(gen_func):

    def wrapper(*args, **kwargs):

        gen = gen_func(*args, **kwargs)
        next(gen)
        return gen

    return wrapper


@auto_start
def accumulator():

    total = 0

    while True:
        x = yield total

        if x is not None:
            total += x


gen2 = accumulator()

print(gen2.send(5))
print(gen2.send(3))