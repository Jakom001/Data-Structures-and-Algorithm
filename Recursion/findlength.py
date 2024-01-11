# find the length of a string

def findLength(text):
    if text == "":
        return 0

    return findLength(text[:-1]) + 1


text = "Victoria"

result = findLength(text)
print(result)
