#!/usr/bin/python3
def element_at(my_list, idx):
    leng = len(my_list)
    if idx < 0 or idx + 1 > leng:
        return None
    else:
        return my_list[idx]
