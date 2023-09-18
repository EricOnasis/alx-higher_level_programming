#!/usr/bin/python3

"""Class Square definition"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class initialization"""
    def __init__(self, size, x=0, y=0, id=None):
        """Dunder function"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
