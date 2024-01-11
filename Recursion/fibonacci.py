def fibonacci(n):
    if n ==0 or n==1:
        return n

    return fibonacci(n-2) + fibonacci(n-1)

n = 5
for i in range(n):
    result = fibonacci(i)
    print(result)
