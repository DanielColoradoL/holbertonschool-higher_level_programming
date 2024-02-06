#!/usr/bin/python3
"""
Module containing say_my_name function only
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - prints a hello massega
        adding a first name and a last name
        if no last name is provided, it will
        only print the first name
        checks if first and last name are strings


    args:
        first_name: string representing a first name
        last_name: string representing a last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
