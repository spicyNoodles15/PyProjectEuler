"""
###PROBLEM 6###
# https://projecteuler.net/problem=6 #
Sum square difference

"""
##Track Execution time##
import time
start = time.time()
########################

# Variables #
num = 100

def sum_of_squares(num):
    total = 0
    for x in range(1,num+1):
        total += x ** 2
    return total

def square_of_sum(num):
    total = 0
    for x in range(1,num+1):
        total += x
    return total ** 2

# Print results of calculations #
print("Sum Square Difference: " + str(square_of_sum(num)-sum_of_squares(num)))

##Print Execution Time##
end = time.time()
print(f"Execution time: {end-start}s")
########################