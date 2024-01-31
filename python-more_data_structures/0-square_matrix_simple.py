#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    output = [row[:] for row in matrix]
    for row in output:
        row[:] = map(lambda x: x * x, row)
    return output
