def get_kmp_array(s):
    """
    Computes the KMP (Knuth-Morris-Pratt) array for a given string `s`.
    
    The KMP array (or prefix table) is used to identify the longest prefix 
    which is also a suffix for each substring `s[0:i]`. This table helps in 
    pattern matching by allowing us to skip certain comparisons.

    Args:
        s (str): The input string for which the KMP array is computed.

    Returns:
        list: A list representing the KMP array for the input string `s`.
    """
    n = len(s)                  # Length of the input string
    kmp = [0] * (n + 1)         # Initialize KMP array with zeros, extra element for 1-based indexing
    
    kmp[0] = -1                 # Start with -1 to handle boundary conditions for prefix matching
    cur = 0                     # Current index in the input string `s`
    match_pos = -1              # Tracks position in `s` for prefix match

    # Process the string to fill the KMP array
    while cur < n:
        # Fall back if there's a mismatch between s[cur] and s[match_pos]
        while match_pos != -1 and s[cur] != s[match_pos]:
            match_pos = kmp[match_pos]  # Move back to the previous prefix position

        # Increment match position and current character index in `s`
        match_pos += 1
        cur += 1

        # Store the length of the longest prefix-suffix match for current position
        kmp[cur] = match_pos

    return kmp


# Example usage
s = "abbaabbab"
kmp = get_kmp_array(s)
print(kmp)  # Expected output: [-1, 0, 0, 0, 1, 1, 2, 3, 4, 2]

# Explanation of expected output:
# str = [    a  b  b  a  a  b  b  a  b]
# kmp = [-1, 0, 0, 0, 1, 1, 2, 3, 4, 2]

# STRING MATCHING EXAMPLE
s = "sadbutsad"
p = "sad" 
res = get_kmp_array(f"{p}#{s}") 
print(res)

#      0  1  2  3  4  5  6  7  8  9  10 11 12
#      s  a  d  #  s  a  d  b  u  t  s  a  d
# [-1, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 3]