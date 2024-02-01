#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for index in range(0, x):
            print(my_list[index], end="")
            count = count + 1
        print()
    except IndexError:
        print()
    return count
