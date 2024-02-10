#!/usr/bin/python3
"""Module containing append_write function"""


def append_write(filename="", text=""):
    """Append text to a file
    Return the number of chars added"""
    with open(filename, 'a', encoding="utf-8") as f:
        b = f.tell()
        f.write(text)
        a = f.tell()
        return a - b
