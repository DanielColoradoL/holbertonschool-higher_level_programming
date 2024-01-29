#!/usr/bin/python3
def uniq_add(my_list=[]):
    output = 0
    for num in my_list:
        if my_list.count(num) == 1:
            output = output + num
    return output
