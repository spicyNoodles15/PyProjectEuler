"""
PROBLEM 1
https://projecteuler.net/problem=1
Multiples of 3 or 5

"""

# Track Execution time
import time
start = time.time()

total = 0
for x in range(1, 1000):
    if x%3==0 or x%5==0:
        total+=x
print(total)

# Print Execution Time
end = time.time()
print(f"Execution time: {(end-start):.3f}s")
