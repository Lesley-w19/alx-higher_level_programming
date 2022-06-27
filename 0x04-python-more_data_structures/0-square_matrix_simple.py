#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = matrix.copy()
    for row in range(len(n_matrix)):
        n_matrix[row] = list(map(lambda x: x ** 2, n_matrix[row]))
    return n_matrix
