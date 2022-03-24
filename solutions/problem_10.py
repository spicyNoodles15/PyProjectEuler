"""
PROBLEM 10
https://projecteuler.net/problem=10
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
# Libraries
import math
import time

# Variables #
NUMBER = 2_000_000

def solution():
    '''
    Solution 10
    '''

    # Track Execution time
    # start = time.time()

    # Print results of calculations #
    # print("Summation of primes: " + str(add_primes(NUMBER)))

    # Print Execution Time
    # end = time.time()
    # print(f"Execution time: {(end-start):.3f}s")

    return add_primes(NUMBER)

def check_for_prime(l_num):
    """
    Returns True/False after testing input for prime
    """
    # Check for divisible by 2 and 3 so we can ignore those multiples in the for loop
    if l_num <= 1:
        return False
    if l_num == 2:
        return True
    if l_num > 2 and l_num % 2 == 0:
        return False
   
    #Now loop through the remaining range using only odd numbers
    for z in range(3,math.floor(math.sqrt(l_num))+1,2):
        if l_num%z==0:
            return False
    return True

def add_primes(l_num):
    """
    Add prime numbers
    """
    total = 0
    if l_num == 2:
        return 2
    if l_num == 3:
        return 5
    if l_num == 7:
        return 12
    if l_num > 7:
        for y in range(1,l_num+1):
            if check_for_prime(y):
                total += y
    return total

def sol_text():
    '''
    Text of problem 10
    '''
    return '''Summation of primes:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''