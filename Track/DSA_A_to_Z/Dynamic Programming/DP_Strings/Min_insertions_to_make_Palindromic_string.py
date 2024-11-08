"""

PROBLEM:
- Given a string S. In one step you can insert any character at any index of the string.
- Return the minimum number of steps to make s palindrome.

SOLUTION
- Worst way of doing -> reverse entire string and attach it to last (BUT WE WANT MIN)
- To make str into palindrome how many min insertions you need?
- Some chars of str can already be a palindrome -> LONGEST PALINDROMIC SUBSEQUENCE
- res = len(str) - len(lps)


HOW?
str = mbadm, lps=mam (u wont touch mam since its already a palindrome)
- m |b| a |d| m
-> you can make this: [m |db| a |bd| m] OR [m |bd| a |db| m]
- IMP: So you can insert chars not present in LPS into the opposite half to make entire string as palindrome
- Since we can insert anything anywhere so MIN INSERTIONS = len(str) - len(lps)
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

    def lps(self, s: str) -> int:
        return self.find_lcs(s, s[::-1])

    def minInsertions(self, s: str) -> int:
        return len(s)-self.lps(s)
      
