#!/usr/bin/python3
"""ALX SE interview question"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D matrix 90 degrees clockwise.
    l = left, r = right
    b = bottom, t = top

    Args:
        matrix (list[[list]]): matrix
    """
    l, r = 0, len(matrix) - 1

    while l < r:
        for m in range(r - l):
            t, b = l, r

            top_lft = matrix[t][l + m]
            matrix[t][l + m] = matrix[b - m][l]
            matrix[b - m][l] = matrix[b][r - m]
            matrix[b][r - m] = matrix[t + m][r]
            matrix[t + m][r] = top_lft
        l += 1
        r -= 1
