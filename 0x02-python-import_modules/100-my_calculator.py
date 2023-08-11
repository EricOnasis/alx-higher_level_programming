#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":

    argument_count = len(argv)

    if argument_count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))

    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))

    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))

    elif operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
