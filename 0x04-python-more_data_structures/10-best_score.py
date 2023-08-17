#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    top_mark = 0
    max_key = 0

    for key, value in a_dictionary.items():
        if value > top_mark:
            top_mark = value
            max_key = key

    return max_key
