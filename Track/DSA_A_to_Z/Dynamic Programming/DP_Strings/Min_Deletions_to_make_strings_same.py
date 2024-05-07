"""
PROBLEM:
- Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
- In one step, you can delete exactly one character in either string


SOLUTION:
- You need to delete chars from s1 and s2 to make it equal
- LCS gives you max common chars in order
- So then LCS chars are kept fixed in both strings, and remaining chars are deleted
  RES =  len(S1)-LCS + len(S2)-LCS
"""

class Solution:
    def find_lcs(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        if n1 == 0 or n2==0:
            return 0
        dp = [[0 for _ in range(n2+1)]  for _ in range(n1+1)]

        for i in range(n1+1):
            for j in range(n2+1):
                if i==0 or j==0:
                    dp[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        # print(*dp, sep="\n")
        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        lcs =  self.find_lcs(word1,word2)
        return len(word1)-lcs + len(word2)-lcs