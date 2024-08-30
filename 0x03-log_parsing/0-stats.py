#!/usr/bin/env python3
""" 0. Log parsing """

import sys


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
log = {"file_size": 0, "code_list": {str(code): 0 for code in status_codes}}
line_count = 0

for line in sys.stdin:
    args = line.split(' ')
    if len(args) > 2:
        file_size = args[-1]
        status_line = args[-2]

    if status_line in log['code_list']:
        if status_line.isdecimal():
            log["code_list"][status_line] += 1

    log["file_size"] += int(file_size)
    line_count += 1

    if line_count == 10:
        print("File size: {}".format(log["file_size"]))

        sorted_codes = sorted(log["code_list"].keys())
        
        for key in sorted_codes:
            value = log["code_list"][key]
            if value != 0:
                print(f"{key}: {log['code_list'][key]}")
        line_count = 0

