#!/usr/bin/python3
"""This module contains the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Read the private width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Modify the private width attribute"""
        self.__width = width

    @property
    def height(self):
        """Read the private height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Modify the private height attribute"""
        self.__height = height

    @property
    def x(self):
        """Read the private x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Modify the private x attribute"""
        self.__x = x

    @property
    def y(self):
        """Read the private y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Modify the private y attribute"""
        self.__y = y
