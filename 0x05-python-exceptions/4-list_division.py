#!/usr/bin/python3

my_list = []
for item in range(0, list_length):
    try:
        div = my_list_1[item] / my_list_2[item]
    except TypeError:
        print("wrong type")
        div = 0
    except ZeroDivisionError:
        print("division by 0")
        div = 0
    except IndexError:
        print("out of range")
        div = 0
    finally:
        my_list.append(div)
return (my_list)
