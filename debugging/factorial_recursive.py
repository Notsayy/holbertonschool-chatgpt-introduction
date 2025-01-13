#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input number `n`. If `n` is 0, returns 1 as 0! = 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
