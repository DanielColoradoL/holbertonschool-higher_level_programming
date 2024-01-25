#!/usr/bin/env python3
def print_last_digit(number):
    x = number
    if x < 0:
        x = -x
    print(x % 10, end="")
    return (x % 10)
