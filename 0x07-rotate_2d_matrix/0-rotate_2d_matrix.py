#!/usr/bin/env python3
""" Rotate 2D Matrix
"""
def rotate_2d_matrix(matrix):
    R, C = len(matrix), len(matrix[0])
    newArr = [[None] * R for x in range(C)]
    for c in range(C):
        for r in range(R):
            newArr[r][c] = matrix[C-1-c][r]
    return newArr
