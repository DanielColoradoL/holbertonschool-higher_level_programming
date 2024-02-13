#!/usr/bin/python3
"""This module contains the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")

        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """Read the private height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Modify the private height attribute"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """Read the private x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Modify the private x attribute"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """Read the private y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Modify the private y attribute"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """Computes the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints rectangle with #"""
        for i in range(self.y):
            print()

        for row in range(self.__height):
            for j in range(self.x):
                print(" ", end="")

            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Adds the print feature to the class"""
        l1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -"
        l2 = f" {self.__width}/{self.__height}"
        return l1 + l2

    def update(self, *args):
        """Update the Rectangle values based on *args"""
        leng = len(args)

        if leng >= 1:
            self.id = args[0]
        if leng >= 2:
            self.__width = args[1]
        if leng >= 3:
            self.__height = args[2]
        if leng >= 4:
            self.__x = args[3]
        if leng == 5:
            self.__y = args[4]
