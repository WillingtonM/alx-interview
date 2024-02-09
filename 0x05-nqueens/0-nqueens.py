#!/usr/bin/python3
"""
    N queens solution finder module.
"""
import sys

sols = []
n_size = 0
postn = None


def get_input():
    """
        Retrieves validates program's argument
        Returns (int): chessboard size
    """
    global n_size
    n_size = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n_size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n_size


def is_attacking(pos_0, pos_1):
    """
        Checks if positions of two queens are in an attacking mode.
        Args:
            pos_0 (list or tuple): 1st queen's position.
            pos_1 (list or tuple): 2nd queen's position.
        Returns (bool): True if queens are in attacking position else False.
    """
    if (pos_0[0] == pos_1[0]) or (pos_0[1] == pos_1[1]):
        return True
    return abs(pos_0[0] - pos_1[0]) == abs(pos_0[1] - pos_1[1])


def group_exists(group):
    """
        Checks if group exists in list of solutions.
        Args: group (list of integers): group of possible positions.
        Returns (bool): True if exists, False otherwise.
    """
    global sols
    for stn in sols:
        s_cnt = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    s_cnt += 1
        if s_cnt == n_size:
            return True
    return False


def build_sols(row, group):
    """
        Builds solution for n queens problem.
        Args:
            row (int): Current row in chessboard.
            group (list): Group of valid positions.
    """
    global sols
    global n_size
    if row == n_size:
        tmp_grp = group.copy()
        if not group_exists(tmp_grp):
            sols.append(tmp_grp)
    else:
        for col in range(n_size):
            a = (row * n_size) + col
            sol_matches = zip(list([postn[a]]) * len(group), group)
            pos_used = map(lambda x: is_attacking(x[0], x[1]), sol_matches)
            group.append(postn[a].copy())
            if not any(pos_used):
                build_sols(row + 1, group)
            group.pop(len(group) - 1)


def get_sols():
    """
        Gets solutions for given chessboard size.
    """
    global postn, n_size
    postn = list(map(lambda x: [x // n_size, x % n_size], range(n_size ** 2)))
    a = 0
    group_sol = []
    build_sols(a, group_sol)


n_size = get_input()
get_sols()
for sol in sols:
    print(sol)
