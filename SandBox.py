import random

numbers = [random.randint(1, 1000) for _ in range(10)]

print(numbers)
print(numbers[1:])
count = 1
numbers_2 = [if i > numbers[count - 1:] for i in numbers[1:]]