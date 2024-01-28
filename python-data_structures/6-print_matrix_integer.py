#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for val in list:
            print("{:d}".format(val), end=" ")
        print()
