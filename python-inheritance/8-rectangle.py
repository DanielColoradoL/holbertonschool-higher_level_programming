#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represent a Rectangle
    Inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Creates a new instance of rectangle
        It validates width and height
        using integer_validator
        inherited from BaseGeometry

        args:
            width = rectangle width
            height = rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
