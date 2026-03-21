'''
Создай декоратор, который автоматически запускает генератор.

Чтобы можно было писать:

gen = accumulator()
gen.send(5)
gen.send(3)

без:
next(gen)

📋 Требования
Сделай декоратор:

@auto_start
def accumulator():

Он должен:

1️⃣ создать генератор
2️⃣ автоматически сделать next(gen)
3️⃣ вернуть готовый генератор

📋 Пример использования
@auto_start
def accumulator():
    total = 0
    while True:
        x = yield total
        if x is not None:
            total += x

Теперь должно работать:

gen = accumulator()

print(gen.send(5))
print(gen.send(3))


Вывод:

5
8

📌 Подсказка

Декоратор должен выглядеть примерно так:

def auto_start(func):


Внутри нужно:

вызвать функцию

получить генератор

сделать next()

вернуть его

💡 Почему это важно

Этот паттерн реально используется в книгах вроде
Fluent Python
и в старых coroutine-библиотеках Python.

🎯 Твоя задача

Написать:

auto_start decorator


и проверить:

gen.send()
работает без next()

'''

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





if __name__ == '__main__':

    gen2 = accumulator()

    print(gen2.send(5))
    print(gen2.send(3))


