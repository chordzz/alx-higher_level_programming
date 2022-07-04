#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Funtion that returns True if an object is an instance of a class
        and false otherwise

        Args:
            obj: object to check
            a_class: Class to compare with

        Returns:
            True or False
    """
    return isinstance(obj, a_class)
