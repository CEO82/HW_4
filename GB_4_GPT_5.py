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

    i = 1
    while i <= 10:


        try:

            yield i
            i += 1


        except RuntimeError:
            print(f'Function is on pause')
            i += 1


        except StopIteration:
            print(f'Generator is finishing')
            print(f'Final number is {i}')
            return



if __name__ == '__main__':
    gen = pausable_counter()

    try:
        print(next(gen))
        print(next(gen))
        gen.throw(RuntimeError)
        print(next(gen))
        gen.throw(StopIteration)
        print(next(gen))
        print(next(gen))


    except StopIteration:
        print(f'Generator finaly finished')




