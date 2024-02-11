#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys


def generate_sols(row, column):
    """
    solve simple N x N matrix
    Args:
        row: # of rows
        column: # of columns
    Returns:
        returns a list of lists
    """
    sols = [[]]
    for queen in range(row):
        sols = queen_placing(queen, column, sols)
    return sols


def queen_placing(queen, column, prev_sols):
    """
    Place queen at certain position
    Args:
        queen: Queen
        column: Column to move
        prev_sols: Previous move
    Returns: list
    """
    safe_pos = []
    for arr in prev_sols:
        for y in range(column):
            if safety(queen, y, arr):
                safe_pos.append(arr + [y])
    return safe_pos


def safety(q_, x_, array):
    """
    check if safe to make move
    Args:
        q: row to move to
        x: column to move to
        array (array): the matrix
    Returns: boolean
    """
    if x_ in array:
        return (False)
    else:
        return all(abs(array[column] - x_) != q_ - column
                   for column in range(q_))


def init():
    """
        Initialize game
        Args: function takes no args
        Returns: returns integer
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():
    """
        Main entry point
        Args: can be called without passing args
        Returns None
    """
    n = init()
    sols = generate_sols(n, n)
    for arr in sols:
        clean_sol = []
        for p, q in enumerate(arr):
            clean_sol.append([p, q])
        print(clean_sol)


if __name__ == '__main__':
    n_queens()
