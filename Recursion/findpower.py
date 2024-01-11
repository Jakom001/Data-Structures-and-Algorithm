# Find the power of a number 
def findpower(base, power):

    if power == 0:
        return 1
    return base * findpower(base, power-1) 
base = 2
power = 3 
result = findpower(base, power)
print(result)

# Output 8
