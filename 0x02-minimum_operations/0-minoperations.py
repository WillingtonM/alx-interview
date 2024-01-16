#!/usr/bin/python3
"""
Module to return Minimum Operations
Given num n, write a method that calculates fewest number of operations
to result in exactly n H characters in file
"""


def minOperations(n):
    """
    Minimum Operations function
    Returns: integer, otherwise return 0
    """
    res = 0
    j = 2
    while n > 1:
        while n % j == 0:
            res += j
            n /= j
        j += 1
    return res
