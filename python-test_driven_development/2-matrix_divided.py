#!/usr/bin/python3
"""
Module containing matrix_divided function only
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - divide matrix by div
        checks if matrix is a list of lists
        checks if the sublists have the same lenght
        checks if all the values are either integers of floats
        checks if div is not 0 and it's either a integer or float
        proceed to divide matrix / div

    args:
        matrix: list of lists (values must be integers or floats)
        div: divisor (must be an integer or float different than 0)

    Return:
        output_list = returns a new list of lists w all values divided by div
    """
    if not isinstance(matrix, list):
        raise (TypeError
              ("matrix must be a matrix (list of lists) of integers/floats"))

    flag = 0
    for sub_list in matrix:
        for value in sub_list:
            if type(value) not in [int, float]:
                raise (TypeError
                      ("matrix must be a matrix (list of lists) "
                       "of integers/floats"))
        if not isinstance(sub_list, list):
            raise (TypeError
                  ("matrix must be a matrix (list of lists) "
                   "of integers/floats"))
        if flag == 0:
            sub_list_len = len(sub_list)
            flag = 1
        else:
            if sub_list_len != len(sub_list):
                raise (TypeError
                      ("Each row of the matrix must have the same size"))
            sub_list_len = len(sub_list)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    output_list = []
    output_sublist = []
    for sub_list in matrix:
        for value in sub_list:
            output_sublist.append(round(value / div, 2))
        output_list.append(output_sublist)
        output_sublist = []

    return output_list
