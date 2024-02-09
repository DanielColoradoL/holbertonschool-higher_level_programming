#!/usr/bin/python3
""" Module containing BaseGeometry class  """


class BaseGeometry():
    """ Represent a BaseGeometry """

    def area(self):
        """ area raise an exception as
        it has not been implemented yet """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates an integer

        args:
            name = string representing a name
            value = value to validate """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
