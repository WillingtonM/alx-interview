#!/usr/bin/python3
""" UTF-8 Validation module
"""


def validUTF8(data):
    """ Method checks if a list of integers are valid UTF-8 codepoints.
    """
    bytes_num = 0

    msk_1 = 1 << 7
    msk_2 = 1 << 6

    for d in data:

        mask_byte = 1 << 7

        if bytes_num == 0:

            while mask_byte & d:
                bytes_num += 1
                mask_byte = mask_byte >> 1

            if bytes_num == 0:
                continue

            if bytes_num == 1 or bytes_num > 4:
                return False

        else:
            if not (d & msk_1 and not (d & msk_2)):
                    return False

        bytes_num -= 1

    if bytes_num == 0:
        return True

    return False
