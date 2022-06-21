#!/usr/bin/python3
"""Class called square with attribute called size"""


class Square:
    """Class called Square with attribute called size"""

    def __init__(self, size=0):
        """Square Constructor"""

        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
