#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    output = a_dictionary.copy()
    if key in output.keys():
        output[key] = value
    else:
        output.update({key: value})
    return (output)
