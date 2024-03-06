#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates perimeter of island described in grid

    Args (grid):
        2d list of integers containing 0 [water] or 1 [land]
    Return: perimeter of the island
    """

    perim = 0
    for x in range(len(grid)):
        for j in range(len(grid[x])):
            if (grid[x][j] == 1):
                if (x <= 0 or grid[x - 1][j] == 0):
                    perim += 1
                if (x >= len(grid) - 1 or grid[x + 1][j] == 0):
                    perim += 1
                if (j <= 0 or grid[x][j - 1] == 0):
                    perim += 1
                if (j >= len(grid[x]) - 1 or grid[x][j + 1] == 0):
                    perim += 1
    return perim
