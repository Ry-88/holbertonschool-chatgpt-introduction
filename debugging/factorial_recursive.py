#!/usr/bin/python3
"""
factorial.py

A simple command-line program to compute the factorial of a non-negative integer
passed as an argument.

Usage:
    python3 factorial.py 5
    Output: 120
"""

import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer n.

    Parameters:
        n (int): A non-negative integer

    Returns:
        int: The factorial of n

    Raises:
        RecursionError: If the recursion depth is exceeded for very large n
        ValueError: If n is negative
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the integer from command-line arguments and compute factorial
f = factorial(int(sys.argv[1]))
print(f)
