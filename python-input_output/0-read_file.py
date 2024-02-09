#!/usr/bin/python3
"""Module containing read_file function"""


def read_file(filename=""):
    """Reads a file"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
