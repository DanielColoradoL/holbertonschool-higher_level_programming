#!/usr/bin/python3
"""Module containing to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns a JSON representation
    of an object (string)"""
    return json.dumps(my_obj)
