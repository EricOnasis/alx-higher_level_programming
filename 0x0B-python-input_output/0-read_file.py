#!/usr/bin/python3

"""A module containing a function that reads a file"""


def read_file(filename=""):
    """A function that reads a file"""
    with open(filename, "r", encoding="utf-8") as myfile:
        for lines in myfile:
            print(lines, end="")
