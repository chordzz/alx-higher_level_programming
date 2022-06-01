#!/usr/bin/python3
def print_last_digit(number):
    rem = abs(number) % 10
    if number < 0:
        rem = -rem
    print("{}".format(rem), end="")
    return rem
