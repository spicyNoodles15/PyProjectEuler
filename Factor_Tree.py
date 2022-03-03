
import math
from math import sqrt

##Track Execution time##
import time
start = time.time()
########################
# vars
divisors = []
test = 0
largest = 0
div_lookup = 500

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


def factor_tree(num):
    factors=[]
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
    return factors

# find the x'th triangle number
def triangle_num(num):
    if num == 1:
        return 1

    # now test all other nums
    triangle = 0
    for x in range(1, num+1):
        triangle += x
    return triangle

# Function Calls
#find the x'th triangle number
while len(divisors) <= div_lookup:
    tri = triangle_num(test)
    divisors = factor_tree(tri)
    if len(divisors) > largest:
        largest = len(divisors)
        curr = time.time()
        print(f"Current Largest divisors {largest}, elapsed time: {curr-start}s")
    if len(divisors) >= div_lookup:
        print(f"The First Triangle number with at least {div_lookup} divisors is {tri}")
        break
    else:
        test += 1 

# print(*factors, sep=",")
# print(len(factors))


##Print Execution Time##
end = time.time()
print(f"Execution time: {end-start}s")
########################