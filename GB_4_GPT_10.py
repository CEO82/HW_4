'''
🔹 Цель

Создать несколько калькуляторов, которые выполняют команды параллельно и используют await + asyncio.sleep для имитации работы.

🔹 Шаги
Создать асинхронный калькулятор:
import asyncio

async def async_calculator(name):
    total = 0
    commands = [5, 10, 'get', 3, 'reset', 7]

    for cmd in commands:
        await asyncio.sleep(1)  # имитация работы
        if isinstance(cmd, (int, float)):
            total += cmd
            print(f"{name}: total = {total}")
        elif isinstance(cmd, str):
            cmd_lower = cmd.lower()
            if cmd_lower == 'get':
                print(f"{name}: total = {total}")
            elif cmd_lower == 'reset':
                total = 0
                print(f"{name}: reset to 0")
        # игнорируем всё остальное
Создать несколько калькуляторов:
async def main():
    tasks = [
        asyncio.create_task(async_calculator("Calc A")),
        asyncio.create_task(async_calculator("Calc B")),
        asyncio.create_task(async_calculator("Calc C")),
    ]

    await asyncio.gather(*tasks)
Запустить:
asyncio.run(main())
🔹 Что проверяем
Все калькуляторы запускаются параллельно
Каждый выводит свои результаты с задержкой 1 сек
Команды get и reset корректно обрабатываются
Используются async def, await и asyncio.create_task
🔹 Бонус (по желанию)
Сделать генерацию команд случайной длины
Использовать разное время asyncio.sleep() для имитации разных скоростей

💡 Подсказка:
await asyncio.sleep(x) не блокирует event loop — это как твой yield в прошлом, но теперь параллельно.


'''

import asyncio

async def multi_calculator(name):
    total = 0
    commands = [7, 11, 'get', 35, 'reset', 77, 15, 33]
    timer = [1, 5, 3, 1, 5, 2, 3, 1]

    for cmd, time in zip(commands, timer):

        await asyncio.sleep(time)
        if isinstance(cmd, (float, int)):
            total += cmd
            print(f'Function-> {name} and summ -> {total}')

        elif isinstance(cmd, str):

            lower_cmd = cmd.lower()
            if lower_cmd == 'get':
                print(f'Function-> {name} and summ -> {total}')

            elif lower_cmd == 'reset':
                total = 0
                print(f'Function-> {name} reset to 0\nand summ -> {total}')





async def main():

    tasks = [
        asyncio.create_task(multi_calculator('Calc A')),
        asyncio.create_task(multi_calculator('Calc B')),
        asyncio.create_task(multi_calculator('Calc C'))

    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':

    asyncio.run(main())

