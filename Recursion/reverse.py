# Reverse a string

def reverse(word):
    if word == "":
        return ""
    return reverse(word[1:]) + word[0]

letter = "john"
result = reverse(letter)
print(result)  

# Output nhoj

