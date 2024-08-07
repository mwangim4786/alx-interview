#!/usr/bin/python3
"""Function for pascals triangle"""

def pascal_triangle(n):
    """
    Creates a function def pascal_triangle(n) that returns a list
    of lists of integers representing the Pascal’s triangle of n:
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n - 1):
        temp = [0] + triangle[-1] + [0]
        new_row = []
        for j in range(len(triangle[-1]) + 1):
            new_row.append(temp[j] + temp[j + 1])
        triangle.append(new_row)
    return triangle
