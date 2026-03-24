'''
Создать двухуровневую coroutine, где основной генератор делегирует работу подгенератору через yield from и
корректно передаёт/возвращает значения.

Шаги
1.  Создать подгенератор subgen():
Принимает через send() числа и накапливает их в total
Когда получает строку 'get', возвращает текущий total через yield
Когда получает строку 'reset', сбрасывает total = 0
Любые другие значения игнорирует

def subgen():
    total = 0
    while True:
        cmd = yield total
        # здесь логика обработки

2. Создать основной генератор main_gen():
Делегирует работу subgen() через yield from
После завершения subgen (через return) возвращает результат в виде yield result

def main_gen():
    result = yield from subgen()
    yield result

3. Проверка

g = main_gen()
print(next(g))         # старт
print(g.send(5))       # 5
print(g.send(10))      # 15
print(g.send('get'))   # 15
print(g.send('reset')) # 0
print(g.send(3))       # 3


!!! - Критерии
Используется yield from для делегирования subgen
Подгенератор обрабатывает send() и yield корректно
Возврат через return проксируется наружу
Любые некорректные команды игнорируются

'''

def subgen():
    total = 0
    while True:
        cmd = yield total
        if isinstance(cmd,(int, float)) and not isinstance(cmd, bool):
            total += cmd
        else:
            if isinstance(cmd, str):
                cmd_lower = cmd.lower()
                if cmd_lower == 'get':
                    continue
                elif cmd_lower == 'reset':
                    total = 0

                elif cmd_lower == 'stop':
                    return total
                else:
                    print(f'Wrong command')
            else:
                print(f'Wrong input')



def main_gen():

    result = yield from subgen()
    yield result


if __name__ == '__main__':

    g = main_gen()
    print(next(g))  # старт
    print(g.send(5))  # 5
    print(g.send(10))  # 15
    print(g.send('get'))  # 15
    print(g.send('reset'))  # 0
    print(g.send(3))  # 3
    print(g.send('stop'))
