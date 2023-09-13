#!/usr/bin/python3

"""A module that contains a function that appends to a textfile"""


def append_write(filename="", text=""):
    """A function that appends to a textfile"""
    with open(filename, "a", encoding="utf-8") as myfile:
        return (myfile.write(text))
