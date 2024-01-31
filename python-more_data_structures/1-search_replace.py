#!/usr/bin/python3
def search_replace(my_list, search, replace):
    output = my_list.copy()
    for i, num in enumerate(output):
        if num == search:
            output[i] = replace
    return output
