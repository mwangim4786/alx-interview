#!/usr/bin/python3
""" 0. Log parsing - Write a script that reads stdin line by line and computes metrics: """

import sys


line_count = 0
sum_file_size = 0
status_code = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

try:
    for line in sys.stdin:
        args = line.split(' ')
        if len(args) > 2:
            status_line = args[-2]
            file_size = args[-1]
            if status_line in status_code:
                status_code[status_line] += 1
            sum_file_size += int(file_size)
            line_count += 1
            if line_count == 10:
                print('File size: {:d}'.format(sum_file_size))
                sorted_keys = sorted(status_code.keys())
                for key in sorted_keys:
                    value = status_code[key]
                    if value != 0:
                        print('{}: {}'.format(key, value))
                line_count = 0
except Exception:
    pass
finally:
    print('File size: {:d}'.format(sum_file_size))
    sorted_keys = sorted(status_code.keys())
    for key in sorted_keys:
        value = status_code[key]
        if value != 0:
            print('{}: {}'.format(key, value))

