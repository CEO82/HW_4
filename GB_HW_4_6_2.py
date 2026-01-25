'''6. Реализовать два небольших скрипта:
● итератор, генерирующий целые числа, начиная с указанного;
● итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
повторение элементов списка прекратится.
'''
from decimal import Decimal
from itertools import cycle, count, takewhile

def number_gen():

    while True:
        print(f'\nThis function is for number generation')
        start_finish_check = input(f'\nIf you want to start this function please enter any symbol, \nif you want o finish this function enter q or Q, next function will start automatically, \nYour choice: ').lower()
        if start_finish_check == 'q':
            print(f'\nProgram is finished by user choice')
            break
        try:
            start_num = float(input(f'Please enter a starting number: '))
            generator_step = float(input(f'Please enter a number for generator step: '))
            finish_num = float(input(f'Please enter a last number: '))

        except ValueError:
            print(f'\nYou are entered something wrong please repeat input ')
            continue
        num_list = takewhile(lambda x: x <= finish_num, count(start_num, generator_step))
        print(list(num_list))

def in_out_fr_num_gen():

    pass









if __name__ == '__main__':
    print()
    x = number_gen()