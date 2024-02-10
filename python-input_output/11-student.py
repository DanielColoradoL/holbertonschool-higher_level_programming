#!/usr/bin/python3
"""Module containing Student Class"""
import os
import sys

class Student():
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with basic attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary with simple data structure
        If no attrs are given, returns all key, value pairs
        If attrs are given, It only returns a dictionary
        with the given keys in it"""
        if attrs is None:
            return self.__dict__

        output_dic = {}
        for key in self.__dict__:
            if key in attrs:
                output_dic[key] = self.__dict__.get(key)
        return output_dic

    def reload_from_json(self, json):
        """Update attributes based on a JSON
        dictionary"""
        self.first_name = json.get("first_name")
        self.last_name = json.get("last_name")
        self.age = json.get("age")
