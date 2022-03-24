"""
PROBLEM 5
https://projecteuler.net/problem=5
Smallest multiple

2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

# Track Execution time
import time
start = time.time()

# Variables
MAX_DIVISOR = 20
RANGE = 1_000_000_000

def solution():
    '''
    Solution 5
    '''

    # Track Execution time
    # start = time.time()

    # print("Smallest multiple: " + str(smallest_multiple(MAX_DIVISOR)))

    # Print Execution Time
    # end = time.time()
    # print(f"Execution time: {(end-start):.3f}s")

    return smallest_multiple(MAX_DIVISOR)

def smallest_multiple(num):
    """
    Returns smallest multiple of input
    """
    # local Variables
    divisible = True

    for x in range(1, RANGE):
        for y in range(2, num+1):
            if x % y != 0:
                divisible = False
                break
            else: divisible = True

            if y == MAX_DIVISOR and divisible is True:
                return x

def sol_text():
    '''
    Text of problem 5
    '''
    return '''Smallest multiple:

2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
'''
