

import sys

def main():
    # sys.argv — это список аргументов, переданных в программу
    # sys.argv[0] — это имя самого файла
    # sys.argv[1:] — всё, что идёт после него
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: python calc.py <num1> <num2> <operation>")
        return

    num1, num2, op = args
    num1 = float(num1)
    num2 = float(num2)

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print("Unknown operation")

if __name__ == "__main__":
    main()