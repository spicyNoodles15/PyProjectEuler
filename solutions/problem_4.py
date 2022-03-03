"""
###PROBLEM 4###
# https://projecteuler.net/problem=4 #
Largest palindrome product

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
##Track Execution time##
import time
start = time.time()
########################

for x in reversed(range(1, 1000)):
    test = x * (x - 1)

    if palindrome_test(number) and number > largest_palindrome:
        largest_palindrome = number

def palindrome_test(num):

    return answer







##Print Execution Time##
end = time.time()
print(f"Execution time: {end-start}s")
########################