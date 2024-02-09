#!/usr/bin/python3
"""Module containing print_sorted"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj inherits from a_class
    False otherwise"""
    if isinstance(obj, a_class):
        return True
    return False
