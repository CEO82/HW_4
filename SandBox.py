from itertools import count, takewhile


# Логика итератора (отдельно)
def my_count_iterator(start, step, stop):
    # Возвращаем объект итератора
    return takewhile(lambda x: x <= stop, count(start, step))


def run_task_1():
    print("--- Задание 1: Генератор чисел ---")
    try:
        start = float(input("Старт: "))
        step = float(input("Шаг: "))
        stop = float(input("Финиш: "))

        gen = my_count_iterator(start, step, stop)

        # Печатаем элементы по одному, как и положено итератору
        for num in gen:
            print(num, end=" ")
        print("\nГотово!")
    except ValueError:
        print("Ошибка: нужно вводить числа.")


if __name__ == '__main__':
    run_task_1()