#!/usr/bin/python3
"""
    Class of a Rectangle and it's various methods,
    and attributes
"""


class Rectangle:
    """
    Class of a Rectangle and it's various methodsg
    and attributes
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructor method to initialize various attributes
        of the rectangle

        width(default=0) of type int
        height(default=0) of type int
        """

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ Method to print the string representation of our class
            works for when we call print() and str() """

        if self.__width == 0 or self.__height == 0:
            return ""

        printable = []
        for x in range(self.__height):
            printable.append(str(self.print_symbol) * self.__width)

        return "\n".join(printable)

    def __repr__(self):
        """
        Method to return the string representation of the rectangle
        to be able to create a new instance
        """
        return ('{}'.format(Rectangle(self.__width, self.__height)))

    def __del__(self):
        """ Method that runs when an instance is to be destroyed """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the biggest area
            Args:
                - rect_1 :type(Rectangle)
                - rect_2: type(Rectangle)
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
