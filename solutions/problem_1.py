"""
PROBLEM 1
https://projecteuler.net/problem=1
Multiples of 3 or 5
"""

# Track Execution time
import time
start = time.time()

# Variables
total = 0
RANGE = 1000

for x in range(1, RANGE):
    if x%3==0 or x%5==0:
        total+=x
print(total)

# Print Execution Time
end = time.time()
print(f"Execution time: {(end-start):.3f}s")
