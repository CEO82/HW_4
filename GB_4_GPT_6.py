'''
🔹 Задание: Logging Accumulator

Создай генератор logging_accumulator():
Начальное значение: 0
При каждом send(value) генератор добавляет value к аккумулятору
При каждом yield генератор возвращает текущую сумму
Генератор должен обрабатывать ошибки через throw(ValueError):
Если прилетает ValueError, печатать "Invalid value, skipping" и не изменять сумму
Генератор можно закрывать через close() → печатать "Accumulator finished"

🔹 Пример использования
gen = logging_accumulator()

print(next(gen))         # старт, сумма 0
print(gen.send(5))       # сумма 5
print(gen.send(3))       # сумма 8
gen.throw(ValueError)    # Invalid value, skipping
print(gen.send(2))       # сумма 10
gen.close()              # Accumulator finished

Вывод должен быть примерно:

0
5
8
Invalid value, skipping
10
Accumulator finished

💡 Подсказка:

Используй конструкцию x = yield total → двусторонняя связь с генератором
send() передаёт значение внутрь генератора
throw() позволяет генератору реагировать на исключения
close() можно ловить через GeneratorExit
'''

def logging_accumulator():

    total = 0
    x = 'No Input!'
    print(f'Accumulator had started\nTotal sum is {total}')

    while True:

        try:

            x = yield total
            if x is not None:
                total += x
                print(f'*******************\nReceived     -> {x}')
                print(f'Current sum -> {total}\n*******************')


        except GeneratorExit:
            print(f'Accumulator is finishing\nlast input was {x}\nTotal summ is {total}')
            print(f'Accumulator had finished')
            return

        except ValueError:
            print(f'Invalid value, skipping')
            print(f'\nTotal summ is {total}\n')


def gen_control():
    gen_launch = logging_accumulator()
    next(gen_launch)
    while True:

        start_close = input(f'If you want start or continue program input Y or y'
                            f'\nif you want to close program input any other symbol -> ')

        if start_close.lower() != 'y':

            gen_launch.close()
            return

        else:

            try:

                num_input = float(input(f'Input number to store in Accumulator -> '))



            except ValueError:

                gen_launch.throw(ValueError)
                continue

            gen_launch.send(num_input)







if __name__ == '__main__':
    gen_control()

