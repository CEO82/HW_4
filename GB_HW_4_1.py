'''1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
'''

if __name__ != '__main__':
    print(f'\nThis file is not for import!!!')

import sys


def salary():
    args = sys.argv[1:]

    if len(args) != 3:
        print(
            f'\nYou need to enter 3 arguments: worked hours, hour rate and extra bonus\nPlease restart the program and enter arguments')
        return

    w_hours, h_rate, ex_bonus = args

    try:
        work_hours = float(w_hours)
        hour_rate = float(h_rate)
        extra_bonus = float(ex_bonus)

        return work_hours * hour_rate + extra_bonus

    except:
        print(f'\nYou are entered wrong value, please repeat enter again')
        return


if __name__ == '__main__':

    result = salary()

    if result is not None:
        print(f'The salary for the Emploee will be: {result} UK Pounds')
