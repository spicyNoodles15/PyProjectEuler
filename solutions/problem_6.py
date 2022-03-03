"""
PROBLEM 6
https://projecteuler.net/problem=6
Sum square difference
"""

# Track Execution time
import time
start = time.time()

# Variables
NUM = 100

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

# Print results of calculations #
print("Sum Square Difference: " + str(square_of_sum(NUM)-sum_of_squares(NUM)))

# Print Execution Time
end = time.time()
print(f"Execution time: {(end-start):.3f}s")
