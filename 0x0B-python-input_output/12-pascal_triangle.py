#!/usr/bin/python3
"""
a function def pascal_triangle(n):
that returns a list of lists of integers representing the
Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """_summary_
    Pascal’s triangle of n:
    Args:
        n (_type_): size of the pascal triangle
    """

    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(n):
            if j > i:
                break
            if i > 0 and len(triangle) == i and len(triangle[i - 1]) == j:
                y = triangle[i - 1][j]
            elif len(triangle) >= i:
                y = 0
            if (
                i > 0 and len(triangle) > i - 1 and 
                j > 0 and len(triangle[i - 1]) > j - 1
            ):
                x = triangle[i - 1][j - 1]
            else:
                x = 0
            if x == 0 and y == 0:
                row.append(1)
            else:
                row.append(x + y)
            triangle.append(row)

        return triangle