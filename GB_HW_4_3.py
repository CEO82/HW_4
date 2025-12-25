"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""

def multiple_of_20_21():
    return (n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0)

if __name__ == '__main__':
    print(f'\nThe Result list is: {list(multiple_of_20_21())}')