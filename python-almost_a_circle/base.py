#!/usr/bin/python3
"""This module contains the Base class"""


class Base():
    """Defines the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        If id not provided it will
        assing a unique value"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
