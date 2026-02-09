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

def number_generator(last_number):
    for n in range(1, last_number + 1):
        yield n





if __name__ == '__main__':
    print(number_generator(11))
    for i in number_generator(11):
        print(i)

    pass