#!/usr/bin/python3
"""Module containing Student Class"""


class Student():
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with basic attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns a dictionary with simple data structure"""
        return self.__dict__
