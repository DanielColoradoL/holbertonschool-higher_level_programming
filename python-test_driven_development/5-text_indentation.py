#!/usr/bin/python3
"""
Module containing say_my_name function only
"""


def text_indentation(text):
    """
    text_indentation - Print the input text
        split by '.', '?', ':'
        add a new line after one
        of the previous chars are found
        It checks that text is a string

    args:
        text: the string to split
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for index, char in enumerate(text):
        if char in ['.', '?', ':']:
            if index < len(text):
                index += 1
            print(text[start: index])
            print()
            if text[index] == " ":
                index += 1
            start = index
    print(text[start: index + 1], end="")
