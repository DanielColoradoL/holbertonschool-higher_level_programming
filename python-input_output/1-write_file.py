#!/usr/bin/python3
"""Module containing write_file function"""


def write_file(filename="", text=""):
    """Write a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return f.tell()
