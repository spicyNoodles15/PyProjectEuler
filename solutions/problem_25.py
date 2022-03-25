"""
PROBLEM 25
https://projecteuler.net/problem=25
1000-digit Fibonacci number

"""
# Libraries
import time


def solution():
    '''
    Solution 25
    '''

    # Variables #
    curr_index = 2
    fib_list = [1,1] # init fibonacci list
    RANGE = 1000
    digit_count = 0

    # Track Execution time
    start = time.time()

    while digit_count < RANGE:
        # add next number to the fibonnaci sequence
        fib_list.append(fib_list[-2] + fib_list[-1])
        # check to see if latest number reaches the RANGE
        digit_count = len(str(abs(fib_list[-1])))
        # increment curr_index
        curr_index+=1

    # Print Execution Time
    end = time.time()
    print(f"Execution time: {(end-start):.3f}s")

    return curr_index


def sol_text():
    '''
    Text of problem 25
    '''
    return '''1000-digit Fibonacci number:
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''