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

        self.__height = height
        self.__width = width

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
            raise ValueError("width must be >= 0")
        if type(value) != int:
            raise TypeError("width must be an integer")
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
            raise ValueError("height must be >= 0")
        if type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value
