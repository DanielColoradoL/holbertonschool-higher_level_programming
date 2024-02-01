#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    output = a_dictionary.copy()
    if key in output:
        output.pop(key)
    return output
