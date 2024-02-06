#!/usr/bin/python3
"""
Module containing matrix_divided function only
"""


def print_square(size):
    """
    print_square - Prints a square made of #
        Using size as an input
        it checks if size is an integer or
        if it is a float and less than 0
        it also checks if it is an int < 0

    args:
        size: the size of the desired square
    """
    if (not isinstance(size, int) or
       isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
