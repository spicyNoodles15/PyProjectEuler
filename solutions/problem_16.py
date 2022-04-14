"""
PROBLEM 16
https://projecteuler.net/problem=16

"""
# Libraries
import time

# Variables #
POWER = 1000

def solution():
    '''
    Solution 16
    '''

    # Track Execution time
    start = time.time()

    # local vars
    answer = 0

    # Get product
    prod = pow(2,POWER)
    # convert to string so we can get individual digits
    prod_str = str(prod)
    # add each digit
    for num in prod_str:
        answer += int(num)

    # Print Execution Time
    end = time.time()
    print(f"Execution time: {(end-start):.3f}s")

    # print(f'Answer: {answer}')
    return answer

def sol_text():
    '''
    Text of problem 16
    '''
    return '''Power digit sum:

2^15 = 32768 and the sum of its digits is 3+2+7+6+8 = 26.

What is the sum of the digits of the number 2^1000?
'''