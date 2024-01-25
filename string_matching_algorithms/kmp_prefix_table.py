def compute_lps_array(pattern):
    # start with F[0] = 0
    lps = [0]
    # temporary value
    c = 0
    # start from 1 because we already have F[0] = 0
    for i in range(1, len(pattern)):
        # in case of a pattern match
        if pattern[c] == pattern[i]:
            # increase substring length by 1
            c = c + 1 
        # else if pattern matches the first character
        elif pattern[i] == pattern[0]:
            c = 1
        # if the pattern doesn't match the subsequence or the first character
        else:
            # reset substring length to 0
            c = 0
        # Fail function F[i] = c
        lps.append(c)
        
    return lps

# example usage 
pattern = "ABABACA"
lps_result = compute_lps_array(pattern)
print(f"The LPS array for pattern '{pattern}' is: {lps_result}")
