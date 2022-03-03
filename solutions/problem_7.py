"""
PROBLEM 7
https://projecteuler.net/problem=7
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

# Libraries
import math
import time

# Track Execution time
start = time.time()

# Variables
NUMBER = 10001

def check_for_prime(num):
    """
    Returns True/False after testing input for prime
    """
    # Check for divisible by 2 and 3 so we can ignore those multiples in the for loop
    if num <= 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False

    #Now loop through the remaining range using only odd numbers
    for z in range(3,math.floor(math.sqrt(num))+1,2):
        if num%z==0:
            return False
    return True

def count_primes(num):
    """
    count the number of primes
    """
    # local variables
    count = 0
    y = 1

    while count < num:
        if check_for_prime(y):
            count += 1
            y += 1
        else:
            y += 1
    return y-1

# Print function result#
print(f'{NUMBER} prime: {str(count_primes(NUMBER))}')

# Print Execution Time
end = time.time()
print(f"Execution time: {(end-start):.3f}s")
