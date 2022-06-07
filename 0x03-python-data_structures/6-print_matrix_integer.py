#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            if (column != 0):
                print(' ', end='')
            print("{:d}".format(column), end='')
        print()
