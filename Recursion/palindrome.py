# Check if a string is a palindrome or not
def palindrome(word):
    if word == "" or len(word) == 1:
        return True

    if word[0] == word[-1]:
        return palindrome(word[1:len(word) - 1])
    
    return False

result = palindrome('madam')
print(result)
