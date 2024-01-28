#!/usr/bin/python3
"""
script that reads stdin line by line & computes metrics:
"""
import sys
x = 0
size_file = 0
code_status = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
               '404': 0, '405': 0, '500': 0}

try:
    for line in sys.stdin:
        args = line.split(' ')
        if len(args) > 2:
            line_status = args[-2]
            file_size = args[-1]
            if line_status in code_status:
                code_status[line_status] += 1
            size_file += int(file_size)
            x += 1
            if x == 10:
                print('File size: {:d}'.format(size_file))
                keys_sorted = sorted(code_status.keys())
                for k in keys_sorted:
                    val = code_status[k]
                    if val != 0:
                        print('{}: {}'.format(k, val))
                x = 0
except Exception:
    pass
finally:
    print('File size: {:d}'.format(size_file))
    keys_sorted = sorted(code_status.keys())
    for k in keys_sorted:
        val = code_status[k]
        if val != 0:
            print('{}: {}'.format(k, val))
