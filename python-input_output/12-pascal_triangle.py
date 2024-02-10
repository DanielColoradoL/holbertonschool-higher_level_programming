#!/usr/bin/python3
"""Module containing pascal_triangle"""


def pascal_triangle(n):
    """Represents a pascal triangle"""
    if n <= 0:
        return []

    outer_list = []
    num_1 = 0
    num_2 = 0

    for i in range(n):
        inner_list = []
        for j in range(i + 1):
            if i < 2 or j == 0 or j == i:
                sum = 1
            else:
                num_1 = outer_list[i - 1][j - 1]
                num_2 = outer_list[i - 1][j]
                sum = num_1 + num_2
            inner_list.append(sum)
        outer_list.append(inner_list)
    return outer_list
