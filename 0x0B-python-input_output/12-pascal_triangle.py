#!/usr/bin/python3
"""
a function def pascal_triangle(n):
that returns a list of lists of integers representing the
Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """_summary_
    Pascal’s triangle of n:
    --- using recursive method
    Args:
        n (_type_): size of the pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle

    triangle = [[0 for x in range(i + 1)] for i in range(n)]
    triangle[0] = [1]

    for i in range(1, n):
        triangle[i][0] = 1
        for j in range(1, i + 1):
            if j < len(triangle[i - 1]):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            else:
                triangle[i][j] = triangle[i - 1][0]
    return triangle
