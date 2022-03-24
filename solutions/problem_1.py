"""
PROBLEM 1
https://projecteuler.net/problem=1
Multiples of 3 or 5
"""
import time

def solution():
    '''
    Solution 1 function
    '''

    # Track Execution time
    start = time.time()

    # Variables
    total = 0
    RANGE = 1000

    for x in range(1, RANGE):
        if x%3==0 or x%5==0:
            total+=x

    # Print Execution Time
    end = time.time()
    print(f"Execution time: {(end-start):.3f}s")
    return total

def sol_text():
    '''
    Text of problem 1
    '''
    return '''Multiples of 3 or 5:

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''
