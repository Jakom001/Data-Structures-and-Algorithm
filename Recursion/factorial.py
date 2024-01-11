# factorial of a number
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

n = 5
result = factorial(n)
print(result)       # Output 120

