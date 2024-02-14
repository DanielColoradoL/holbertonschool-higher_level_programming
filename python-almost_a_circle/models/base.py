#!/usr/bin/python3
"""This module contains the Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string from
        list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return an object based on a JSON string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string into a JSON file"""
        with open(cls.__name__ + ".json", 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                output = []
                for object in list_objs:
                    dic = object.to_dictionary()
                    output.append(dic)
                f.write(cls.to_json_string(output))
