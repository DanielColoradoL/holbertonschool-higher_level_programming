#!/usr/bin/python3
"""Module containing save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """writes a JSON representation of an object
    in a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
