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

def return_n(last_number: int):
    for i in range(1, last_number + 1):
        return i



def generate_n(last_number: int):

    pass





if __name__ == '__main__':

    pass