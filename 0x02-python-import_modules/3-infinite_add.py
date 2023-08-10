#!/usr/bin/python3

if __name__ == "__main__":
    import sys

sum = 0
numbers = len(sys.argv) - 1

for item in range(numbers):
    sum = sum + int(sys.argv[item + 1])

print("{}".format(sum))
