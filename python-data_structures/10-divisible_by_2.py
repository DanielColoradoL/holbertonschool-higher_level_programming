#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [i for i in range(len(my_list))]
    i = 0
    for val in (my_list):
        if val % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
        i += 1
    return (new_list)
