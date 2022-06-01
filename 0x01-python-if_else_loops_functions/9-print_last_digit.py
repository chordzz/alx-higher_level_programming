#!/usr/bin/python3
def print_last_digit(number):
    rem = abs(number) % 10
    if number < 0:
        return -rem
    return rem
