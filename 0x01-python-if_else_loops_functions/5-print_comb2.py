#!/usr/bin/python3

for num in range(0, 100):
    if num < 98:
        print("{:02}, ".format(num), end="")

    if num == 98:
        print("{}".format(num))
