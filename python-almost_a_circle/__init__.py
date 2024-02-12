#!/usr/bin/python3
"""This module contains the Base class"""


class Base():
    """Defines the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
