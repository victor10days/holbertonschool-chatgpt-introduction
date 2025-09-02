#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        This function calculates the factorial of a given integer.
        
    Parameters:
        n (int): The input integer for which the factorial needs to be calculated.

    Returns:
        int: The calculated factorial value.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)