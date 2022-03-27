
"""
PROBLEM 4
https://projecteuler.net/problem=4
Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

# libraries
import time

def solution():
    """
    Find the largest palindrome number from product of two 3-digit numbers
    """
    # Track Execution time
    start = time.time()

    largest_palindrome = 0

    # loop from largest 3 digit number
    for x in reversed(range(1, 1000)):
        # inner loop in reverse starting with current x
        for y in reversed(range(1,x)):
            test = x * y
            # test if palindrome and if it's larger thand current largest found
            if palindrome_test(test) and test > largest_palindrome:
                largest_palindrome = test

    # Print Execution Time
    end = time.time()
    print(f"Execution time: {(end-start):.3f}s")

    return largest_palindrome

def palindrome_test(num):
    """
    Test if a number is a palindrome by using string split method
    """
    string_value = str(num)
    return bool(string_value == string_value[::-1])

def sol_text():
    '''
    Text of problem 4
    '''
    return '''Largest palindrome product:

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
