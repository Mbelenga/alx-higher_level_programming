#!/usr/bin/python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of integers representing the pascal's triangle
    of n
    Returns an empty list of n <= 0
    Assume n will be always an integer
    """
    tri = []
    if n <= 0:
        return tri
    if n == 0:
        return [[1]]

    tri = [[1]]
    for i in range(n-1):
        tri.append([a+b for a, b in zip([0] = tri[-1], tri[-1] + [0])])
        return tri
