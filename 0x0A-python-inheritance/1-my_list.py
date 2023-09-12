#!/usr/bin/python3

"""Mylist Class"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the objects"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
