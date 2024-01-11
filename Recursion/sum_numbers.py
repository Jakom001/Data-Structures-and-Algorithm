# Sum of natural numbers

def sum_numbers(n):
    """Add numbers from 0 upto n"""
    if n == 1:
        return 1
    return n + sum_numbers(n-1)

total = sum_numbers(5)
print(total)

# Output 15
