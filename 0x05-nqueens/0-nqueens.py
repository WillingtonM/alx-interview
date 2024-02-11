#!/usr/bin/python3
"""
    N queens solution finder module.
"""
import sys


def backtracks(rw, nm, culumns, pos, neg, board):
    """
    function: backtrack to find solution
    """
    if rw == nm:
        res = []
        for b_len in range(len(board)):
            for k_len in range(len(board[b_len])):
                if board[b_len][k_len] == 1:
                    res.append([b_len, k_len])
        print(res)
        return

    for k in range(nm):
        if k in culumns or (rw + k) in pos or (rw - k) in neg:
            continue

        culumns.add(k)
        pos.add(rw + k)
        neg.add(rw - k)
        board[rw][k] = 1

        backtracks(rw+1, nm, culumns, pos, neg, board)

        culumns.remove(k)
        pos.remove(rw + k)
        neg.remove(rw - k)
        board[rw][k] = 0


def n_queens(n):
    """
    Solution to n_queens problem
    Args (n): number of queens and must be >= 4
    Returns: List of lists repr. coordinates of each
        queen for all possible solutions
    """
    negv_diag = set()
    posv_diag = set()
    culumns = set()
    board = [[0] * n for k in range(n)]

    backtracks(0, n, culumns, posv_diag, negv_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: n_queens N")
        sys.exit(1)
    try:
        n_n = int(n[1])
        if n_n < 4:
            print("N must be at least 4")
            sys.exit(1)
        n_queens(n_n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
