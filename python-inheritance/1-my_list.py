#!/usr/bin/python3
"""Module containing print_sorted"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Function that returns a new list ordered asc
        copies the original, sort it and return the copy"""
        x = self.copy()
        x.sort()
        return print(x)
