"""
###PROBLEM 10###
# https://projecteuler.net/problem=10 #
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
##Track Execution time##
import time
start = time.time()
########################

import math

# Variables #
num = 2_000_000

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

def add_primes(num):
    total = 0
    if num == 2: return 2
    if num == 3: return 5
    if num == 7: return 12
    if num > 7:
        for y in range(1,num+1):
            if check_for_prime(y): 
                total += y
    return total

# Print results of calculations #
print("Summation of primes: " + str(add_primes(num)))

##Print Execution Time##
end = time.time()
print(f"Execution time: {end-start}s")
########################