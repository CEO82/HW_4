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
from decimal import InvalidOperation
from itertools import cycle, count, takewhile

def number_gen(start_num, step, finish_num):
    return takewhile(lambda x: x <= finish_num if step > 0 else x >= finish_num, count(start_num, step))



def in_out_for_num_gen():
    while True:
        print(f'\nThis function is for number generation')
        start_finish_check = input(f'\nIf you want to start this function please enter any symbol, \nif you want o finish this function enter q or Q, next function will start automatically, \nYour choice: ').lower()
        if start_finish_check == 'q':
            print(f'\nProgram is finished by user choice')
            break
        try:
            start_num = Decimal(input(f'Please enter a starting number: '))
            step = Decimal(input(f'Please enter a number for generator step: '))
            finish_num = Decimal(input(f'Please enter a last number: '))
            if step == 0:
                print(f'You are entered step = 0, this is forbiden, please repeat input')
                continue
            elif step < 0 and finish_num > start_num:
                print(f'You are entered negative step and finish number greater than start number \nIt is prohibited, please repeat input')
                continue
            elif step > 0 and finish_num < start_num:
                print(
                    f'You are entered positive step and finish number smaller than start number \nIt is prohibited, please repeat input')
                continue




        except (ValueError, InvalidOperation):
            print(f'\nYou are entered something wrong please repeat input ')
            continue



        for num in number_gen(start_num,step, finish_num):
            print(f'| {num}', end=' | ')


def cycle_traffik_light():

    pass




if __name__ == '__main__':
    print()
    in_out_for_num_gen()