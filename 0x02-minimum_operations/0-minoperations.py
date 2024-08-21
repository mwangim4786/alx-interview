#!/usr/bin/env python3
""" 
Minimum Operations
"""

def minOperations(n):
    """
    Method that calculates the fewest number of operations needed 
    to result in exactly n H characters 
    """
    
    if n <= 1:
        return 0
    
    div = 2
    operations = 0

    while n > 1:
        if n % div == 0:
            n = n / div
            operations = operations + div
        else:
            div +=1
    
    return operations

