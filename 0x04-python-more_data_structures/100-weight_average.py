#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    dev = 0

    for item in my_list:
        num += item[0] * item[1]
        dev += item[1]

    return (num / dev)
