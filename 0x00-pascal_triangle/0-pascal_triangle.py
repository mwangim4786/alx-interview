#!/usr/bin/python3
"""
Creates a function def pascal_triangle(n) that returns a list of lists of integers representing the Pascal’s triangle of n:
"""

def pascal_triangle(n):
    triangle = [[1]]

    for i in range(n - 1):
        temp = [0] + triangle[-1] + [0]
        new_row = []
        for j in range(len(triangle[-1]) + 1):
            new_row.append(temp[j] + temp[j + 1])
        triangle.append(new_row)
    return triangle





    # return [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

