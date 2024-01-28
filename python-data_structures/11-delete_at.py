#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    leng = len(my_list)
    if leng == 0 or idx >= leng:
        return (my_list)
    key = my_list[idx]
    my_list.remove(key)
    return (my_list)
