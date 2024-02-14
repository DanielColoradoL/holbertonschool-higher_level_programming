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
