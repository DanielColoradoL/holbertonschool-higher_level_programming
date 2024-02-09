#!/usr/bin/python3
"""Module containing print_sorted"""


def is_same_class(obj, a_class):
    """Returns true if obj and a_class are
    exactly the same, False otherwise"""
    if type(obj) is a_class:
        return True
    return False
