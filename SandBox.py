

import asyncio

async def worker(name, queue):
    total = 0

    while True:
        cmd, delay = await queue.get()

        await asyncio.sleep(delay)

        if isinstance(cmd, (int, float)):
            total += cmd
            print(f'{name}: total = {total}')

        elif cmd == 'get':
            print(f'{name}: total = {total}')

        elif cmd == 'reset':
            total = 0
            print(f'{name}: reset to 0')

        queue.task_done()


async def main():
    queue = asyncio.Queue()

    # добавляем задачи
    commands = [
        (7, 1),
        (11, 2),
        ('get', 1),
        (35, 2),
        ('reset', 1),
    ]

    for item in commands:
        await queue.put(item)

    # запускаем воркер
    task = asyncio.create_task(worker("Calc A", queue))

    # ждём пока очередь обработается
    await queue.join()

    task.cancel()

asyncio.run(main())



