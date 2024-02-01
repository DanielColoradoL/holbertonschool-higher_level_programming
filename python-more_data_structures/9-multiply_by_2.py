#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    output = a_dictionary.copy()
    for key in output:
        output[key] = output[key] * 2
    return output
