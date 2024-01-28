#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    leng_1 = len(tuple_a)
    leng_2 = len(tuple_b)
    if leng_1 == 0:
        a = 0
        b = 0
    elif leng_1 < 2:
        a = tuple_a[0]
        b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]
    if leng_2 == 0:
        c = 0
        d = 0
    elif leng_2 < 2:
        c = tuple_b[0]
        d = 0
    else:
        c = tuple_b[0]
        d = tuple_b[1]
    output = (a + c, b + d)
    return output
