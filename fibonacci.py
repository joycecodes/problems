def fib(n, h):
    if (n == 1) or n == 2:
        return 1
    elif n not in h:
        h[n] = (fib(n-1, h) + fib(n-2, h))
    return h[n]


print(fib(400, {}))
