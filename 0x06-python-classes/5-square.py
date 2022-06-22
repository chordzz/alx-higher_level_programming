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

    def area(self):
        """Method that returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Method to print square"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """Method to retrieve the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the private attribute size"""
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
