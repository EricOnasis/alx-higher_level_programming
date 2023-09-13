#!/usr/bin/python3

"""
A module containing a function that writes an
object to a text file (JSON)
"""

import json


def save_to_json_file(my_obj, filename):
    """
    A function that a Json representation
    of an object to a text file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
