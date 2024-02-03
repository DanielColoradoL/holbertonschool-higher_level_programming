#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Represent a square """
    def __init__(self, size=0):
        """
        initializing new objects
        Size must be an integer and > 0
        Else it will raise an error
        Args:
            size: The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area

        Return:
            The area of the square.
        """
        return (self.__size ** 2)
