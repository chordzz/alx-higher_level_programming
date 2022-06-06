#!/usr/bin/python3
def prin_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    for num in reversed(my_list):
        print("{:d}".format(num))
