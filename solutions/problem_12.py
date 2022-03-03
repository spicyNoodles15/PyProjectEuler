"""
###PROBLEM 12###
# https://projecteuler.net/problem=12 #
Highly divisible triangular number


NOT SOLVED!!!!!!!!!!!!!!!!!

"""
##Track Execution time##
import time
start = time.time()
########################

import math
from math import sqrt

# vars
divisors = 0
test = 0
largest = 0
div_lookup = 500

# find the x'th triangle number
def triangle_num(num):
    if num == 1:
        return 1

    # now test all other nums
    triangle = 0
    for x in range(1, num+1):
        triangle += x
    return triangle

# count the number of factors of a number
def count_factors(num):
    if num == 1:
        return 1

    count = 1
    for y in range(1, int((num/2)+1)):
        if num%y==0:
            count += 1
    # return count + 1 to add in the num itself
    return count + 1

while divisors <= div_lookup:
    tri = triangle_num(test)
    divisors = count_factors(tri)
    if divisors > largest:
        largest = divisors
        curr = time.time()
        print(f"Current Largest divisors {largest}, elapsed time: {curr-start}s")
    if divisors >= div_lookup:
        print(f"The First Triangle number with at least {div_lookup} divisors is {tri}")
        break
    else:
        test += 1 

# for i in range(1,8):
#     b = triangle_num(i)
#     print(f"The {i} Triangle Number: {b}, Factors count: {count_factors(b)}")


##Print Execution Time##
end = time.time()
print(f"Execution time: {end-start}s")
########################
