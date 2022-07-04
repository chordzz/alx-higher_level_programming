#!/usr/bin/python3
def lookup(obj):
    """ Lookup function to return the list of available
        attributes and methods of a given object

    Args:
        obj: a given object/ a class

    Returns:
        List of attributes or methods

    """

    return dir(obj)
