"""
PROBLEM 6
https://projecteuler.net/problem=6
Sum square difference
"""

# Track Execution time
import time

# Variables
NUM = 100

def solution():
    '''
    Solution 6
    '''

    # Track Execution time
    start = time.time()

    # Print results of calculations #
    # print("Sum Square Difference: " + str(square_of_sum(NUM)-sum_of_squares(NUM)))

    # Print Execution Time
    end = time.time()
    print(f"Execution time: {(end-start):.3f}s")

    return (square_of_sum(NUM)-sum_of_squares(NUM))

def sum_of_squares(l_num):
    """
    Returns sum of squares
    """
    total = 0
    for x in range(1,l_num+1):
        total += x ** 2
    return total

def square_of_sum(l_num):
    """
    Returns square of sum
    """
    total = 0
    for x in range(1,l_num+1):
        total += x
    return total ** 2

def sol_text():
    '''
    Text of problem 6
    '''
    return '''Sum square difference:
The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,
(1+2+...10)^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025-385=2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
