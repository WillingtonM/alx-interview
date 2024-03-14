#!/usr/bin/python3
""" Prime Game | Maria & Ben are playing game """


def isWinner(x, nums):
    """
    @params:
        x- number of rounds
        nums- array of n
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    lst = [1 for x_num in range(sorted(nums)[-1] + 1)]
    lst[0], lst[1] = 0, 0
    for item in range(2, len(lst)):
        remove_mults(lst, item)

    for item in nums:
        if sum(lst[0:item + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def remove_mults(lst, x):
    """
    removes multiple of primes
    @params:
        ls- list
        x-
    """
    for k in range(2, len(lst)):
        try:
            lst[k * x] = 0
        except (ValueError, IndexError):
            break
