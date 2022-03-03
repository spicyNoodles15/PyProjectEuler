"""
###PROBLEM 7###
# https://projecteuler.net/problem=7 #
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
##Track Execution time##
from itertools import count
import time
start = time.time()
########################

import math

def check_for_prime(num):
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
number = 10001
result = str(count_primes(number))
print(f'{number} prime: {result}')

##Print Execution Time##
end = time.time()
print(f"Execution time: {end-start}s")
########################