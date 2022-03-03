"""
###PROBLEM 2###
# https://projecteuler.net/problem=2 #
###Even Fibonacci numbers####

"""

# Track Execution time
import time
start = time.time()

# VARIABLES
total = 0
fib = [1, 2]

#The problem doesn't ask to generate the fibonoacci list
#but i did anyway so you could use the list in other ways if desired
i = 2
while (fib[i - 1] + fib[i - 2]) < 4_000_000:
    fib.append(fib[i - 1] + fib[i - 2])
    i += 1

for y in fib:
    if y % 2 == 0:
        total += y

print("Sum is: " + str(total))

# Print Execution Time
end = time.time()
print(f"Execution time: {end-start}s")
    