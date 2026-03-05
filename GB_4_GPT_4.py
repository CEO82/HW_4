'''
🧩 Задание — resilient accumulator

Создай генератор:
safe_accumulator()
Он должен:

1️⃣ принимать числа через send()
2️⃣ суммировать их
3️⃣ печатать текущую сумму

НО:
👉 если внутрь прилетает throw(ValueError)
он должен:
вывести "Invalid value received"
НЕ завершаться
продолжить работу

'''

def resilient_accumulator():
    accum = 0
    print(f'\n*******************\nCurrent sum -> {accum}\n*******************')
    while True:
        try:
            x = yield accum
            if x is not None:
                accum += x
                print(f'*******************\nReceived     -> {x}')
                print(f'Current sum -> {accum}\n*******************')
        except ValueError:
            print('**********************\nInvalid value received\n**********************')

        except GeneratorExit:
            print(f'*******************\nFinal sum -> {accum}\nGenerator is closing\n*******************')
            return print('Generator is closed')

def gen_control():
    gen = resilient_accumulator()
    next(gen)
    print(f'Program The "Accumulator" is started!')

    while True:
        continue_or_not = input(f'If you want to continue program, please enter Y or y, \nif not enter any other symbol -> ')
        if continue_or_not.lower() != 'y':
            print(f'Program is going to stop')
            gen.close()
            break

        try:
            num_input = float(input(f'please enter any number -> '))

        except ValueError:
            #print('You entered something wrong, please repeat')
            gen.throw(ValueError)
            continue

        gen.send(num_input)

if __name__ == '__main__':
    gen_control()

