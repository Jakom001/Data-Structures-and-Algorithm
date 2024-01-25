def compute_lps_array(pattern):
    lps = [0]
    c = 0
    for i in range(1, len(pattern)):
        if pattern[c] == pattern[i]:
            c = c + 1 
        elif pattern[i] == pattern[0]:
            c = 1
        else:
            c = 0
        lps.append(c)
    return lps

def kmp(text, pattern):
    lps = compute_lps_array(pattern)
    occurrences = []
    i = 0
    j = 0  # using 'j' to track the position in the pattern
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                occurrences.append((i - j, i - 1))
                j = lps[j - 1]  # resetting 'j' based on LPS array
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences

# example usage
text = "ABABA"
pattern = "ABA"
print(kmp(text, pattern))
