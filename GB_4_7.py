'''7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!. Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''


def factorial_generator(factorial_number: int):
    accumulator = 1
    for i in range(1, factorial_number +1):
        accumulator = accumulator * i
        yield accumulator


if __name__ == '__main__':

    for el in factorial_generator(4):
        print(el)
