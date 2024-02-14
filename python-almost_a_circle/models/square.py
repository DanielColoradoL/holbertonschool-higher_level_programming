#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Adds the print feature to the class"""
        l1 = f"[Square] ({self.id}) {self.x}/{self.y} -"
        l2 = f" {self.width}"
        return l1 + l2

    @property
    def size(self):
        """Read the private size"""
        return self.width

    @size.setter
    def size(self, size):
        """Modify the private size attribute
        It changes width and height underneath"""

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be > 0")

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the Square values based on *args or **kargs"""
        leng = len(args)

        if args is not None and leng > 0:
            if leng >= 1:
                self.id = args[0]
            if leng >= 2:
                self.width = args[1]
            if leng >= 3:
                self.x = args[2]
            if leng == 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "size" in kwargs:
                self.width = kwargs.get("size")
                self.height = kwargs.get("size")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")
