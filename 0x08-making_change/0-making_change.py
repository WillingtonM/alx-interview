#!/usr/bin/python3

""" Coin change making module."""


def makeChange(coins, total):
    """
    Determines fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.

    Returns: 
        - Fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total not met by any number of coins, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change_count = 0
    coins = sorted(coins)[::-1]
    for coin_item in coins:
        while coin_item <= total:
            total -= coin_item
            change_count += 1
        if (total == 0):
            return change_count
    return -1
