'''
Создать генератор, который работает как процесс с состоянием и управляется через send().
1. Генератор с декоратором
@auto_start
def calculator():
2. Внутри генератора
Переменная:
total = 0
Бесконечный цикл:
while True:
3. Приём данных

Генератор должен получать вход через:

cmd = yield total
⚙️ Логика обработки cmd
📥 Если число (int или float)
gen.send(5)

👉 увеличить total:

total += 5
🔁 Если строка 'reset'
gen.send('reset')

👉 сброс:

total = 0
📤 Если строка 'get'
gen.send('get')

👉 просто вернуть текущий total (без изменений)

🚫 Всё остальное

👉 игнорировать (ничего не делать)

📊 Ожидаемое поведение
gen = calculator()

print(gen.send(5))        # 5
print(gen.send(10))       # 15
print(gen.send('get'))    # 15
print(gen.send('reset'))  # 0
print(gen.send(3))        # 3
❗ Важно
❌ не использовать next() вручную
✅ должен работать через @auto_start
✅ использовать send()
✅ всегда возвращать значение через yield
🎯 Критерий готовности

Если этот код работает — задача выполнена:

gen = calculator()

assert gen.send(5) == 5
assert gen.send(10) == 15
assert gen.send('get') == 15
assert gen.send('reset') == 0
assert gen.send(3) == 3


'''

'''program sum calculator'''

def calc_autostart(gen_func):

    def wrapper():
        gen = gen_func()
        next(gen)
        return gen

    return wrapper



@calc_autostart
def calculator():
    total = 0

    while True:
        cmd = yield total
        if isinstance(cmd, (int, float)) and not isinstance(cmd, bool):
            total += cmd
        else:
            if isinstance(cmd, str):
                cmd_lower = cmd.lower()
                if cmd_lower == 'get':

                    continue

                elif cmd_lower == 'reset':
                    total = 0


                else:

                    print(f'wrong command')


            else:
                print(f'wrong enter')




if __name__ == '__main__':

    gen = calculator()

    print(gen.send(5))  # 5
    print(gen.send(10))  # 15
    print(gen.send('get'))  # 15
    print(gen.send(17))
    print(gen.send('reset'))  # 0
    print(gen.send(3))  # 3


