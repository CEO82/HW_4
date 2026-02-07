'''
Создай ДВЕ функции:
1️⃣ Функция return_numbers(n)
Она должна:
принимать n
возвращать список чисел от 1 до n

2️⃣ Генератор yield_numbers(n)
Он должен:
делать то же самое
но через yield

3️⃣ Напиши тест-код, который:
Вызывает обе функции
Выводит:
тип результата (type(...))
результат вывода
Попробует пройтись по результатам через for

'''

def return_numbers(last_number: int):
    name_1 = 'return'
    res_list = []
    for i in range(1, last_number + 1):
        res_list.append(i)

    return res_list



def yield_numbers(last_number: int):
    name_2 = 'yield'
    for m in range(1, last_number + 1):
        yield  m


def user_input():
    while True:
        try:
            last_numb = int(input(f'Enter last number: '))
            if last_numb > 1:
                return last_numb

            else:
                print(f'\nWrong enter, repeat\n')
                continue
        except ValueError:
            print(f'\nWrong enter, repeat\n')
            continue

def print_result(data):
    print(f'\n******')
    print(type(data))
    print(data)
    print(f'******')


def print_result_by_for_in(data):
    print(f'\n******')
    for k in data:
        print(k)

    print(f'******')


def main_function():
    u_input = user_input()
    res_return = return_numbers(u_input)
    res_yield = yield_numbers(u_input)
    print_result(res_return)
    print_result(res_yield)
    print_result_by_for_in(res_return)
    print_result_by_for_in(res_yield)



if __name__ == '__main__':
    main_function()
    pass