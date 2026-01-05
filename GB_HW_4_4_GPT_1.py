"""4. Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в порядке их следования в исходном списке. Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

import random
from collections import Counter

def match_check(init_list):

    counted_list = Counter(init_list)

    return (y for y in init_list if counted_list[y] == 1)

if __name__ == '__main__':
    print(match_check([random.randint(1, 100) for _ in range(30)]))