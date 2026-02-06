'''Напиши генератор count_up_to(n), который:

Принимает число n
Генерирует числа от 1 до n включительно
Использует yield (не список, не return списка)
После достижения n генератор должен корректно завершиться'''


def num_generator(last_numb: int):
    for n in range(1,last_numb):
        yield n

def usr_input():
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




if __name__ == '__main__':
    for i in num_generator(7):
        print(i)


