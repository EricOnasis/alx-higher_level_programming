#!/usr/bin/python3

""" A module that contains a function that
creates object from a Json file. """


import json


def load_from_json_file(filename):
    """
    A function that creates an object from a JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
