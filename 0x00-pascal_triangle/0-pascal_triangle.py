#!/usr/bin/python3
"""
Module for working with Pascal's triangle.
"""


def pascal_triangle(n):
    """Creates list of lists of integers representing
    Pascal's triangle of given integer.
    """
    resList = []
    if n > 0:
        for p in range(1, n + 1):
            lvl = []
            C = 1
            for q in range(1, p + 1):
                lvl.append(C)
                C = C * (p - q) // q
            resList.append(lvl)
    return resList
