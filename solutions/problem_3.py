"""
PROBLEM 3
https://projecteuler.net/problem=3
Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

# Libraries
import math
import time

# Track Execution time
start = time.time()

def check_for_prime(num):
    """
    Checks a number for prime
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

def largest_prime_factor(num):
    """
    Returns largest prime factor of input
    """
    # Find all factors, starting from largest to smallest
    for x in reversed(range(2,math.floor(math.sqrt(num)))):
        # First check if it's a factor
        if num%x==0:
            # Test it for prime
            if check_for_prime(x):
                return x

# Print function result
print("Largest prime: " + str(largest_prime_factor(600851475143)))

# Print Execution Time
end = time.time()
print(f"Execution time: {(end-start):.3f}s")