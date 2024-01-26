#!/usr/bin/python3
"""
script that reads stdin line by line & computes metrics:
"""
import sys

size_total = 0
counter = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}


try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])

            if code in status_codes.keys():
                status_codes[code] += 1

            size_total += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(size_total))

            for k, v in sorted(status_codes.items()):
                if v != 0:
                    print('{}: {}'.format(k, v))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(size_total))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print('{}: {}'.format(k, v))
