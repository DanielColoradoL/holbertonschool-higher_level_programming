#!/usr/bin/python3
"""
Module containing only add_integer function
"""


def add_integer(a, b=98):
    """
    add_integer - adds a and b
        it checks whether the arguments are integer or floats
        then if the arguments are floats, it checks whether
        the arguments are casted to integer
        lastly, it returns an integer with the addition a + b

    args:
        a: first argument to add
        b: second argument to add

    Return:
        the resulting addition casted to integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return int(a + b)
