#!/usr/bin/python3
def uniq_add(my_list=[]):
    output = 0
    tmp = list()
    for num in my_list:
        if tmp.count(num) == 0:
            tmp.append(num)
    for num in tmp:
        output = output + num
    return output
