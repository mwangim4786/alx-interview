#!/usr/bin/env python3
""" 
Minimum Operations
"""

from typing import List

def factors_of(n: int) -> List[int]:
    """ factors of a number n """
    factorsList: List[int] = []

    div: int = 2
    operations: int = 0

    while n > 1:
        if n % div == 0:
            n = n / div

            factorsList.append(div)

            operations = operations + div
        else:
            div +=1

    return factorsList



def minOperations(n: int) -> int:
    """ calculate the minimum operations """
    if type(n) != int or n < 2:
        return 0
    else:
        num_of_operations: int = sum(factors_of(n))
        return num_of_operations
