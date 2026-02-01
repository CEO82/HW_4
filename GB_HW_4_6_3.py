'''6. Реализовать два небольших скрипта:
● итератор, генерирующий целые числа, начиная с указанного;
● итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
повторение элементов списка прекратится.
'''

from itertools import cycle, count, takewhile
from decimal import Decimal, InvalidOperation
from typing import Iterable, Generator, TypeVar
T = TypeVar('T')

def generator_for_count(start_n: Decimal, step: Decimal, finish_n: Decimal):
    return takewhile(lambda x: x <= finish_n if step > 0 else x >= finish_n, count(start_n, step))

def generator_for_cycle(list_for_iteration: list, numbers_of_iterations: int):
    mixed = zip(count(1), list_for_iteration)
    return takewhile(lambda x: x[0] <= numbers_of_iterations, cycle(mixed))

def print_for_generators(generator_obj):
    for p_o in generator_obj: # p_o printing object
        print(f'{p_o}')

def continue_or_not(function_name: str):
    while True:
        user_wish = input(f'If you want to start or continue function {function_name} input any symbol \nif you want to finish function input "q" or "Q"')
        if user_wish.lower() == 'q':
            print(f'Function {function_name} is stopped ')
            return 'stop'

        else:
            continue



def count_funct():
    

    pass

def cycle_funct():

    pass

if __name__ == '__main__':

    print()