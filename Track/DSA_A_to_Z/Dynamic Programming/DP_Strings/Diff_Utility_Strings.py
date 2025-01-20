"""
Problem: Given 2 string, find the len of shortest DIFF_UTILITY strins

s1: XMJYAUZ
s2: XMJAATZ
- Shortest diff string: X M J -Y A -U A T Z

s1: Take all non-sign chars + (all plus sign chars)
s2: Take all non-sign chars + (all minus sign chars)

"""



def solve(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[float("inf") for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    # Base cases
    # Goes over n2 -> all indexes visisted of s2
    for i in range(n1 + 1):
        dp[i][n2] = n1 - i  # Remaining characters of s1
    # Goes over n1 -> all indexes visisted of s1
    for j in range(n2 + 1):
        dp[n1][j] = n2 - j  # Remaining characters of s2

    # Fill DP table bottom-up
    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            if s1[i] == s2[j]:  # Characters match
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:  # Characters differ
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])

    # Reconstruct the shortest diff string
    i, j = 0, 0
    result = []
    while i < n1 or j < n2:
        if i < n1 and j < n2 and s1[i] == s2[j]:  # Match
            result.append(s1[i])
            i += 1
            j += 1
        elif j < n2 and (i == n1 or dp[i][j + 1] <= dp[i + 1][j]):  # Choose from s2
            result.append(f"+{s2[j]}")
            j += 1
        else:  # Choose from s1
            result.append(f"-{s1[i]}")
            i += 1

    print(*dp, sep="\n")  # Optional: Print DP table
    return " ".join(result)

# Example usage
s1 = "XMJYAUZ"
s2 = "XMJAATZ"
print(solve(s1, s2))  # Output: X M J +A -Y A +T -U Z
