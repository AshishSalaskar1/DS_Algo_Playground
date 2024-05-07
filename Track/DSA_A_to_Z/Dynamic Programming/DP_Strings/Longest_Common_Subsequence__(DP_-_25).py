"""
Variations
- Longest Palindromic Subsequence -> LCS(str, reverse(str)
- Min num of insertions or deletion to make string s1=s2
		l = LCS(s1,s2)
		Min Deletions -> len(s1)-l
		Min Insertions -> len(s2)-l
- Shortest Common Subsequence
	1. Given 2 strings, create another string such that it has both the strings as subsequence and is as short as possible
	2. LCS = LCS(str1,str2)
	3. res = LCS + Add missing chars from str1 and str2 in res in order (Such that str1/2 subseq can be formed from res

"""




"""
USE 1 based indexing, because you <0 automatically gets handled
"""

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        if n1==0 or n2==0:
            return 0

        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(n1+1):
            for j in range(n2+1):
                if i==0 or j==0: # no chars left in some string
                    dp[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else: 
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i][j-1]
                    )
        
        return dp[-1][-1]


"""
0-Based Indexing --> TOO COMPLEX
"""


def lcs(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1==0 or n2==0:
        return 0

    dp = [[0 for _ in range(n2)] for _ in range(n1)]

    for i in range(n1):
        for j in range(n2):
            if i==0 and j==0:
                dp[i][j] = 1 if s1[0]==s2[0] else 0
            elif i==0 or j==0:
                #    1. dp=1 if both chars are equal (nothing left in one string to pick in LCS)
                # OR 2. You can ignore the non-zero index in string which has len>0
                # ("b","abc") (0,1) b==b, you cant make any more pair for LCS
                if s1[i]==s2[j]:
                    dp[i][j] = 1
                else:
                    # ("b","bac") (0,1) s1"b"!=s2"a",
                    # but you can still use s2"b" in "bac" to compare with s1"b" to make LCS
                    if i==0: # ("b","bac") (0,1)
                        dp[i][j] = dp[i][j-1]
                    else: # ("bac","b") (1,0)
                        dp[i][j] = dp[i-1][j]
            elif s1[i]==s2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]



CASES
# s1, s2 = "bbbab", "babbb"
# print(*lcs(s1, s2), sep="\n")

# s1, s2 = "def","fed"
# print(*lcs(s1, s2), sep="\n")

# s1, s2 = "adebc","dcadb"
# print(*lcs(s1, s2), sep="\n")

s1, s2 = "abcdb","bcacdhb"
print(*lcs(s1, s2), sep="\n")
print()

CASES
# s1, s2 = "bbbab", "babbb"
# print(*lcs(s1, s2), sep="\n")

# s1, s2 = "def","fed"
# print(*lcs(s1, s2), sep="\n")

# s1, s2 = "adebc","dcadb"
# print(*lcs(s1, s2), sep="\n")

s1, s2 = "abcdb","bcacdhb"
print(*lcs(s1, s2), sep="\n")
print()