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
        Calculate the area of the square

        Return:
            The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Read the private size property
        @property makes the function a property
        Return:
            Size = the size.
        """
        size = self.__size
        return size

    @size.setter
    def size(self, size):
        """
        Modify the private size property
        @size.setter makes the function a setter
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """
        Prints a square made of #
        Using size as an input
        """
        s = self.__size
        if s == 0:
            print()
        for i in range(s):
            for j in range(s):
                print("#", end="")
            print()
