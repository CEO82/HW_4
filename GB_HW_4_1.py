'''1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
'''
import sys

def salary():
    args = sys.argv[1:]

    if len(args) != 3:
        print(f'\nYuo need to enter 3 arguments worked hours, hour rate and extra bonus\nPlease restart the program')
        return


