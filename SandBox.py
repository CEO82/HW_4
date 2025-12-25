import random

def check_list():
    init_list = [random.randint(1, 100) for _ in range(15)]
    print(f'\nInitial list is: {init_list}')

    result_list = [
        curr for prev, curr in zip(init_list, init_list[1:])
        if curr > prev
    ]

    return result_list


if __name__ == '__main__':
    print(f'\nThe Result list is: {check_list()}')