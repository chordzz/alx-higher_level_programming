#!/usr/bin/python3
"""Class called square with attribute called size"""


class Square:
    """Class called Square with attribute called size"""

    def __init__(self, size=0, position=(0, 0)):
        """Square Constructor"""
        self.size = size
        self.position = position

    def area(self):
        """Method that returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Method to print a square"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.position[0], end="")
                print("#" * self.__size)

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

    @property
    def position(self):
        """ Getter for position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (len(value) != 2) or (type(value) != tuple) \
                or (type(value[0]) != int) \
                or (type(value[1]) != int) \
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 integers")
        else:
            self.__position = value
