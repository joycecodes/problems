"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

def collatz(n, cache):
    if n not in cache:
        if n == 1:
            cache[n] = 1
        elif n % 2 == 0:
            cache[n] = 1 + collatz(n/2, cache)
        else:
            cache[n] = 1 + collatz(n * 3 + 1, cache)
    return cache[n]

cache = {}

print(collatz(1000000, cache))