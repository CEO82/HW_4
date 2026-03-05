'''
Задание: Pausable Counter
Создай генератор: pausable_counter()
Он должен:
1️⃣ Считать числа
1
2
3
4
...

каждый раз когда вызывается next().

2️⃣ Поддерживать паузу через throw()

Если внутрь генератора прилетает: gen.throw(RuntimeError) генератор должен: PAUSE RECEIVED

и пропустить один шаг счётчика.

3️⃣ Поддерживать остановку через throw()

Если прилетает:

gen.throw(StopIteration)

генератор должен:

Counter stopped

и корректно завершиться.

'''


def pausable_counter():
    numbers_list = [1, 2, 3, 4, 5, 6]
    while True:


        pass



    pass







if __name__ == '__main__':


    pass