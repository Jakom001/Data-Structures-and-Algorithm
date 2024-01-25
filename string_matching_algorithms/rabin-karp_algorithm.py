def compute_hash(string, base, prime_number):
    length = len(string)
    hash_value = 0

    for i in range(length):
        character_value = ord(string[i])
        exponent = length - i - 1
        term = (character_value * pow(base, exponent)) % prime_number
        hash_value = (hash_value + term) % prime_number

    return hash_value

def rabin_karp(text, pattern):
    base = 256  
    prime_number = 101  
    m = len(pattern)
    n = len(text)
    h = pow(base, m - 1) % prime_number
    p_hash = compute_hash(pattern, base, prime_number)
    t_hash = compute_hash(text[:m], base, prime_number)
    occurrences = []

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if all(text[i + j] == pattern[j] for j in range(m)):
                occurrences.append((i, i + m - 1))
        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime_number
            if t_hash < 0:
                t_hash += prime_number

    return occurrences

# example usage
text = "CODEWITHCODER"
pattern = "CODE"
print(rabin_karp(text, pattern))
