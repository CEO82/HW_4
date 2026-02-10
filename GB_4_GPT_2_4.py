'''
📌 Нужно реализовать
1️⃣ Генератор tap(numbers, label)
Он должен:
принимать поток numbers
принимать строку label
печатать каждое значение с подписью
возвращать значения дальше по pipeline
Пример работы
Если через него проходит число 4:
[filter_even] -> 4
❗ Главное правило
tap НЕ должен менять данные
Он только наблюдает.
📌 Ожидаемое поведение pipeline
Вот примерно так он должен собираться:
pipeline = square_numbers(tap(filter_even(tap(generate_numbers(n),"generate"
)),"filter_even"))

💡 Пример вывода

Для n = 5:

[generate] -> 1
[generate] -> 2
[filter_even] -> 2
4
[generate] -> 3
[generate] -> 4
[filter_even] -> 4
16
[generate] -> 5

⚠️ Подсказки (но без решения)
👉 tap — это обычный генератор
👉 внутри нужно пройтись по входящему потоку
👉 распечатать значение
👉 затем yield его дальше
⭐ Почему это очень крутая практика
Ты научишься:
дебажить pipeline
писать middleware шаги
строить наблюдаемые потоки
понимать ленивость ещё глубже

'''
def user_input():
    while True:
        try:
            last_number = int(input(f'Enter last number -> '))
            if last_number >= 1:
                return last_number
            else:
                print(f'Wrong enter, repeat')
                continue

        except ValueError:
            print(f'Wrong enter, repeat')
            continue

def generate_numbers(last_number):
    for n in range(1, last_number + 1):
        yield n

def filter_even(number_list):
    for e in number_list:
        if e % 2 == 0:
            yield e

def square_numbers(filtered_list):
    for s in filtered_list:
        yield s ** 2

def tap(num_flow, lable):
    for nf in num_flow:
        print(f'{lable} -> {nf}')
        yield nf


if __name__ == '__main__':
    pipeline =  tap(square_numbers(tap(filter_even(tap(generate_numbers(user_input()), 'Generate')), 'Even filter')), 'Square numbers')
    for res in pipeline:
        pass