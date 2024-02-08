#!/usr/bin/python3
""" Defines a Rectangle  """


class Rectangle:
    """ Represent a Rectangle  """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        Deletes an instance of Rectangle
        Print out Bye rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """
        Prints a rectangle made of the
        class variable print_symbol
        Using height and width as input
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print(self.print_symbol, end="")
            if i + 1 != self.height:
                print()
        return ""

    def __repr__(self):
        """
        Prints a representation of the rectangle
        """
        output = f"{self.__class__.__name__}({self.__width}, {self.__height})"
        return output

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

    def area(self):
        """
        Calculate the area of the rectangle

        Return:
            The area of the rectangle.
        """
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Return:
            The perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            per = 0
        else:
            per = 2 * (self.__height + self.__width)
        return per

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares which instance's area is bigger
        checks if rect_1 is an instance of Rectangle
        checks if rect_2 is an instance of Rectangle
        Else it will raise an TypeError
        Args:
            rect_1: Instance of Rectangle
            rect_2: Instance of Rectangle
        Return:
            Return: rect_1 if >= to react_2
                    rect_2 otherwise
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new instance of a Rectangle
        where both heigh and widht are the same
        In other words, a square
        Args:
            size: The size of the new Rectangle
        Return:
            Return: the new instance of Rectangle
        """
        return Rectangle(size, size)
