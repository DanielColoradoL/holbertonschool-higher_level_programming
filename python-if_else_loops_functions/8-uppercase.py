#!/usr/bin/env python3
def uppercase(str):
    output = ""
    for i in (str):
        if 97 <= ord(i) <= 122:
            char_int = ord(i) - 32
            str_char = chr(char_int)
            output = output + str_char
        else:
            output = output + i
    return (print(output))
