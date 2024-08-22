#!/usr/bin/env python3
""" 
Minimum Operations
"""

def factors_of(n):
    """ factors of a number n """
    factorsList = []

    div = 2
    operations = 0

    while n > 1:
        if n % div == 0:
            n = n / div

            factorsList.append(div)

            operations = operations + div
        else:
            div +=1

    return factorsList


def minOperations(n):
    """ calculate the minimum operations """
    if type(n) != int or n < 2:
        return 0
    else:
        num_of_operations = sum(factors_of(n))
        return int(num_of_operations)

