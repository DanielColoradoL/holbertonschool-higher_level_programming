#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Represent a square """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializing new objects
        Size must be an integer and > 0
        Else it will raise an error
        Args:
            size: The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (not isinstance(position, tuple) or
           len(position) != 2 or
           not isinstance(position[0], int) or
           not isinstance(position[1], int) or
           position[0] < 0 or
           position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """
        Read the private position property
        @property makes the function a property
        Return:
            position = tuple with coordinates
        """
        position = self.__position
        return position

    @position.setter
    def position(self, value):
        """
        Modify the private position property
        @position.setter makes the function a setter
        """
        if (not isinstance(value, tuple) or
           len(value) != 2 or
           not isinstance(value[0], int) or
           not isinstance(value[1], int) or
           value[0] < 0 or
           value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints a square made of #
        Also adds lines based on position
        Using size and position as an input
        """
        s = self.__size
        coordinates = self.__position
        if s == 0:
            print()
        for i in range(s):
            for j in range(s):
                for k in range(coordinates[0]):
                    if j == 0:
                        if coordinates[1] > 0:
                            print("_", end="")
                        else:
                            print(" ", end="")
                print("#", end="")
            print()

    def area(self):
        """
        Calculate the area of the square

        Return:
            The area of the square.
        """
        return self.__size ** 2
