'''2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор. Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]. Результат: [12, 44, 4, 10, 78, 123].
'''
import random

def check_list():
    init_list = [random.randint(1, 100) for _ in range(15)]
    print(f'\nInitial list is: {init_list}')
    result_list = []
    count = 1
    for i in init_list[1:]:
        if i > init_list[count - 1]:
            result_list.append(i)
        count += 1
    return result_list




if __name__ == '__main__':
    print(f'\nThe Result list is: {check_list()}')