#!/usr/bin/python3

"""
A module containing a function that
returns a dictionary discription.
"""


def class_to_json(obj):
    """
    Return the dictionary description with a simple
    data structure for JSON serialization of an object.
    """
    return obj.__dict__
