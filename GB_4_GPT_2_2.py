'''
🧩 Задание №4
Создай:
1️⃣ Список квадратов чисел от 1 до 10
Через list comprehension.
2️⃣ Генератор квадратов чисел от 1 до 10
Через generator expression.
3️⃣ Напиши код, который:
выводит тип обоих объектов +
выводит содержимое списка +
выводит содержимое генератора через for +
попробует вывести генератор через print() напрямую +
попробует пройти генератор второй раз
💡 Цель задания — увидеть:
разницу памяти
разницу поведения
одноразовость генераторов
'''

squares_list = [n**2 for n in range(1, 11) ]

def squares_gen():
    for m in range(1, 11):
        yield m**2

def comparison_print(list_print, generator_print):
    print(f'Type of objects\n**************')
    print(f'Type of list -> {type(list_print)}\nType of generator -> {type(generator_print)}\n**************')
    print(f'Contents of objects\n**************')
    print(f'list -> {list_print}\n**************')
    print(f'generator by cycle for -> ')
    for i in generator_print:
        print(i)
    print(f'same generator by print ->\n{generator_print}')
    print(f'generator second time by cycle for -> ')
    for i in generator_print:
        print(i)

def main_func():
    comparison_print(squares_list, squares_gen())

if __name__ == '__main__':
    main_func()

