#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represent a Rectangle
    Inherits from BaseGeometry """

    def __init__(self, size):
        """ Creates a new instance of Square
        It validates size
        using integer_validator
        inherited from Rectangle --> BaseGeometry

        args:
            size = square size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        

    def area(self):
        """Calculates the area"""
        return self.__size ** 2
