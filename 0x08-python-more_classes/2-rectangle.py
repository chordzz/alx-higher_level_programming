#!/usr/bin/python3
"""
    Class of a Rectangle and it's various methods,
    and attributes
"""


class Rectangle:
    """
    Class of a Rectangle and it's various methods,
    and attributes
    """

    def __init__(self, width=0, height=0):
        """
        Constructor method to initialize various attributes
        of the rectangle

        width(default=0) of type int
        height(default=0) of type int
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        getter function for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter function for the width attribute

        Args:
            - Value: int
        """

        if value < 0:
            raise ValueError('width must be >= 0')
        elif type(value) != int:
            raise TypeError('width must be an integer')
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter function for the height attribute
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        setter function for the height attribute

        Args:
            - Value: int
        """

        if value < 0:
            raise ValueError('height must be >= 0')
        elif type(value) != int:
            raise TypeError('height must be an integer')
        else:
            self.__height = value

    def area(self):
        """
        Method to return the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method to return the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
