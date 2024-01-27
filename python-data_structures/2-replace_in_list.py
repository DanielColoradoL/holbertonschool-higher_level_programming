#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    leng = len(my_list)
    if idx < 0 or idx + 1 > leng:
        return my_list
    else:
        my_list[idx] = element
        return my_list
