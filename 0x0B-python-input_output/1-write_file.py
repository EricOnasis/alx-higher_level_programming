#!/usr/bin/python3

"""A module that contains a function that writes to a file"""


def write_file(filename="", text=""):
    "A function that writes to a file"""
    with open(filename, "w", encoding="utf-8") as myfile:
        return myfile.write(text)
