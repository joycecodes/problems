# compute factorial of a number both recursively and iteratively

# iterative
num = 10
factorial = 1
for x in range(1, num + 1):
    factorial = factorial * x
print(factorial)


# recursive
def factorial(value):
    if value == 0:
        return 1
    elif value == 1:
        return value
    else:
        return value * factorial(value - 1)

print(factorial(10))
