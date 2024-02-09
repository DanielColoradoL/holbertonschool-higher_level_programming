#!/usr/bin/python3
"""Module containing inherits_from"""


def inherits_from(obj, a_class):
    """Returns true if obj inherits from a_class
    False otherwise"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
