#!/usr/bin/python3
""" A method that determines if a given data set represents a
    valid UTF-8 encoding.
"""


def validUTF8(data):
    def check(num):
        mask = 1 << 7
        count = 0

        while num & mask:
            mask >>= 1
            count += 1
        return count

    count = 0
    while count < len(data):
        i = check(data[count])
        j = count + i - (i != 0)
        count += 1
        if i ==1 or i > 4 or j >= len(data):
            return False
        while count < len(data) and count <= j:
            val = check(data[i])
            if val != 1:
                return False
            count += 1
    return True
