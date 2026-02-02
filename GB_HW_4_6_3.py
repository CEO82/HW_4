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
    mixed = zip(count(1), cycle(list_for_iteration))
    return takewhile(lambda x: x[0] <= numbers_of_iterations, mixed)

def print_for_generators(generator_obj):
    for p_o in generator_obj: # p_o printing object
        print(f'{p_o}')

def continue_or_not(function_name: str):
    user_wish = input(
        f'If you want to start or continue function {function_name} input any symbol \nif you want to finish function input "q" or "Q" -> ')
    if user_wish.lower() == 'q':
        return False
    else:
        return True

def input_for_count():
    while True:
        try:
            start_num = Decimal(input(f'Please enter a starting number: '))
            step = Decimal(input(f'Please enter a number for generator step: '))
            finish_num = Decimal(input(f'Please enter a last number: '))
            if step == 0:
                print(f'You are entered step = 0, this is forbidden, please repeat input')
                continue
            elif step < 0 and finish_num > start_num:
                print(f'You are entered negative step and finish number greater than start number \nIt is prohibited, please repeat input')
                continue
            elif step > 0 and finish_num < start_num:
                print(
                    f'You are entered positive step and finish number smaller than start number \nIt is prohibited, please repeat input')
                continue
            else:
                return start_num, step, finish_num

        except (ValueError, InvalidOperation):
            print(f'\nYou are entered something wrong please repeat input ')
            continue

def input_for_cycle():
    while True:
        try:
            cycle_reps = int(input(f'Please enter numbers of repeats for cycle ->  '))
        except ValueError:
            print(f'You are entered something incorrectly, please repeat input\n')
            continue
        if cycle_reps <= 0:
            print(f'You are entered number of repeats less or equal to 0, this is forbidden, please repeat input\n')
            continue
        elif cycle_reps > 255:
            print(f'Maximum numbers of repeats is 255, please enter number between 0 and 256\n')
            continue
        else:
            return cycle_reps



def count_funct():
    function_name = '<<count function>>'
    while True:
        if continue_or_not(function_name) is False:
            print(f'Function {function_name} is finished')
            break
        else:
            start_num, step, finish_num = input_for_count()
            print_for_generators(generator_for_count(start_num, step, finish_num))
            continue


def cycle_funct():
    function_name = '<<cycle function>>'
    list_for_iteration = ['Green', 'Yellow', 'Red']
    while True:
        if continue_or_not(function_name) is False:
            print(f'Function {function_name} is finished')
            break
        else:
            numbers_of_iterations = input_for_cycle()
            print_for_generators(generator_for_cycle(list_for_iteration, numbers_of_iterations))



if __name__ == '__main__':
    count_funct()
    cycle_funct()