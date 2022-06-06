#!/usr/bin/python3
def prin_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        my_list.reverse()
        for num in my_list:
            print("{:d}".format(num))
