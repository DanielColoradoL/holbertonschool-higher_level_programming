#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        leng = len(list)
        for j, val in enumerate(list):
            if j == leng - 1:
                print("{:d}".format(val), end="")
            else:
                print("{:d}".format(val), end=" ")
        print()
