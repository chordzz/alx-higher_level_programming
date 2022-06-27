#!/usr/bin/python3
""" function that adds two integers """


def add_integer(a, b=98):
    """Function to add two numbers
    Args:
        a: (int/float)
        b: (int/float)
    Returns:
        Result of adding the two numbers
    Raises:
        TypeError: if a or b are not int/float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
