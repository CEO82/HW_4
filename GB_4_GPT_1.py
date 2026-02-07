'''Напиши генератор count_up_to(n), который:

Принимает число n
Генерирует числа от 1 до n включительно
Использует yield (не список, не return списка)
После достижения n генератор должен корректно завершиться'''


def num_generator(last_numb: int):
    for n in range(1,last_numb + 1):
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

def generators_print(gen_obj):
    for p in gen_obj:
        print(p)


def gpt_gen_test_1():
    generators_print(num_generator(usr_input()))


if __name__ == '__main__':
    gpt_gen_test_1()

