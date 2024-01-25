def brute_force(text, pattern):
    # initialize a list to store positions of pattern occurrences
    occurrences = []  

    for i in range(len(text) - len(pattern) + 1):

        # check if the pattern matches starting from position i
        for j in range(len(pattern)):

            # mismatch found, break the loop
            if text[i + j] != pattern[j]:
                break  
            # whole pattern is matched, record the position
            if j == len(pattern) - 1:
                occurrences.append((i, i + j))  

    return occurrences  

input_text = "CODEWITHCODER"
input_pattern = "CODE"
occurrences = brute_force(input_text, input_pattern)
for occurrence in occurrences:
    print(f"The pattern occurs in the string from index {occurrence[0]} to {occurrence[1]}.")
