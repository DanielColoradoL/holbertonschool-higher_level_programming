#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        print(f"This is key {key} and this is value {value}")
        a_dictionary[key] = value
    else:
        a_dictionary.update({key: value})
    return (a_dictionary)
