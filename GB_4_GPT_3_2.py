'''

🧩 Задание — Logging accumulator
Создай генератор logging_accumulator().
Требования
1️⃣ Накапливает сумму чисел, которые ему отправляют через send().
2️⃣ Выводит текущую сумму при каждом шаге:
Current sum: <текущее значение>
3️⃣ Поддерживает next() — если ничего не послали, просто возвращает текущую сумму.
4️⃣ Поддерживает close() — при закрытии:
выводит итоговую сумму
выводит сообщение о закрытии
корректно завершает генератор
Пример:
Final sum: 17
Closing accumulator...

Пример использования
gen = logging_accumulator()

next(gen)
gen.send(5)
gen.send(10)
gen.send(2)

gen.close()

Ожидаемый вывод:

Current sum: 0
Current sum: 5
Current sum: 15
Current sum: 17
Final sum: 17
Closing accumulator...

Подсказки
Используй try: ... except GeneratorExit:
В цикле while True принимай числа через send()
Проверяй if x is not None
После обработки GeneratorExit генератор должен завершиться (return)
'''

def logging_accumulator():
    accum = 0
    print(f'\n*******************\nCurrent sum -> {accum}\n*******************')
    try:
        while True:
            x = yield accum
            if x is not None:
                accum += x
                print(f'*******************\nReceived     -> {x}')
                print(f'Current sum -> {accum}\n*******************')

    except GeneratorExit:
        print(f'*******************\nFinal sum -> {accum}\nGenerator is closing\n*******************')
        return print('Generator is closed')


if __name__ == '__main__':
    gen = logging_accumulator()

    next(gen)
    gen.send(5)
    gen.close()
    gen.send(10)
    #gen.throw(GeneratorExit)
    gen.send(2)
    #gen.close()
    #del gen


print("Program continues...")
input("Press Enter...")