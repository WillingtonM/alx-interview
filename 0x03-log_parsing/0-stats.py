#!/usr/bin/python3
"""
script that reads stdin line by line & computes metrics:
"""
import sys


def msg_printer(status_code_dict, file_size_total):
    """
    Method to print message
    Args:
        status_code_dict: dictionary of status codes
        file_size_total: total of file
    Returns:
        Nothing
    """

    print("File size: {}".format(file_size_total))
    for k, val in sorted(status_code_dict.items()):
        if val != 0:
            print("{}: {}".format(k, val))


file_size_total = 0
count = 0
code = 0
status_code_dict = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for lne in sys.stdin:
        prsd_line = lne.split()
        prsd_line = prsd_line[::-1]

        if len(prsd_line) > 2:
            count += 1

            if count <= 10:
                file_size_total += int(prsd_line[0])  # file size
                code = prsd_line[1]  # status code

                if (code in status_code_dict.keys()):
                    status_code_dict[code] += 1

            if (count == 10):
                msg_printer(status_code_dict, file_size_total)
                count = 0

finally:
    msg_printer(status_code_dict, file_size_total)
