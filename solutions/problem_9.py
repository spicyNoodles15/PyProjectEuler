"""
PROBLEM 9
https://projecteuler.net/problem=9

"""
# Libraries
import time
from math import sqrt

# Variables #
RANGE = 1000

def solution():
    '''
    Solution 9
    '''

    # Track Execution time
    start = time.time()

    for a in range(1, RANGE):
        for b in range(a+1, RANGE):
            c = sqrt((a*a)+(b*b))
            if c > b:
                if (a+b+c == RANGE) and c.is_integer():
                    # finally determine the product
                    # print(f'Answer: {(a*b*c)}, a={a},b={b},c={c}')

                    # # Print Execution Time
                    # end = time.time()

                    # print(f"Execution time: {(end-start):.3f}s")
                    return int((a*b*c))

    # Print Execution Time
    end = time.time()
    print(f"Execution time: {(end-start):.3f}s")

    return 1

def sol_text():
    '''
    Text of problem 9
    '''
    return '''Special Pythagorean triplet:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
a^2+b^2=c^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''