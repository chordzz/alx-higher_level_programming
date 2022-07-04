#!/usr/bin/python3
""" Class MyList that inherits from the list class """


class MyList(list):
    """ MyList class Derived from the list class """

    def __init__(self):
        super().__init__

    def print_sorted(self):
        """ Method to print the sorted list """
        Llist = self.copy()
        Llist.sort()
        print(Llist)
