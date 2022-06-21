#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for count in range(x):
        try:
            print("{}".format(my_list[count]), end="")
        except IndexError:
            continue

        count += 1
    print()
    return count
