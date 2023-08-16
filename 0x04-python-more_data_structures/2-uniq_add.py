#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    uniq_list = list(uniq_set)
    sum = 0

    for items in uniq_set:
        sum += items
    return sum
