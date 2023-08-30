#!/usr/bin/python3

"""Class definition"""


class Square:
    """Initialization"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of Square"""
        return self.__size * self.__size
