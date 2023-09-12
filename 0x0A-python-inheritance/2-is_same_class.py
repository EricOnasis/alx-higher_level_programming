#!/usr/bin/python3
""" Instance of the same class. """


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.
    Return
        True if the object is exactly an instance
        of the specified class, False otherwise.
    """

    return isinstance(obj, a_class)
