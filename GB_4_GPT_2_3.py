'''
🧩 Задание №5
Создай pipeline обработки чисел:
1️⃣ Генератор generate_numbers(n)
Генерирует числа от 1 до n
2️⃣ Генератор filter_even(numbers)
Принимает генератор чисел
Оставляет только чётные числа
3️⃣ Генератор square_numbers(numbers)
Принимает генератор чисел
Возводит числа в квадрат
4️⃣ Собери pipeline
Типа:
generate_numbers → filter_even → square_numbers
💡 Пример использования
pipeline = square_numbers(filter_even(generate_numbers(10)))
for num in pipeline:
    print(num)
Ожидаемый вывод:
4
16
36
64
100
'''

from itertools import count, takewhile

def generate_numbers():
    for n in range(1, user_input() + 1):
        yield n

def filter_even():
    for e in generate_numbers():
        if e % 2 == 0:
            yield e


def square_numbers():
    for s in filter_even():
        yield s ** 2

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



if __name__ == '__main__':
    pipeline = square_numbers()
    for num in pipeline:
        print(num)

