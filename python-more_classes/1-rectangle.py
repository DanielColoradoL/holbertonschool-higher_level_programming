#!/usr/bin/python3
""" Defines a Rectangle  """


class Rectangle:
    """ Represent a Rectangle  """
    def __init__(self, width=0, height=0):
        """
        initializing new objects
        width must be an integer and > 0
        height must be an integer and > 0
        Else it will raise an error
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Read the private width property
        @property makes the function a property
        Return:
            width
        """
        width = self.__width
        return width

    @width.setter
    def width(self, width):
        """
        Modify the private width attribute
        @width.setter makes the function a setter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        Read the private height property
        @property makes the function a property
        Return:
            height
        """
        height = self.__height
        return height

    @height.setter
    def height(self, height):
        """
        Modify the private height attribute
        @height.setter makes the function a setter
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
