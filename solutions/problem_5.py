"""
###PROBLEM 5###
# https://projecteuler.net/problem=5 #
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
##Track Execution time##
import time
start = time.time()
########################
max_divisor = 20
divisible = True

def smallest_multiple(num):
    for x in range(1, 1_000_000_000):
        for y in range(2, num+1):
            if x % y != 0:
                divisible = False
                break
            else: divisible = True

            if y == max_divisor and divisible == True:
                return x

print("Smallest multiple: " + str(smallest_multiple(max_divisor)))

##Print Execution Time##
end = time.time()
print(f"Execution time: {end-start}s")
########################