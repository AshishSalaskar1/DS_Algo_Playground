"""
Problem: https://leetcode.com/problems/distinct-subsequences/

Solution: Pick/No pick type solution
1. Pick: in case both chars at given index are same
    - dp(i+1,j+1)+dp(i+1,j)
    -> you can either pick or no pick again 
    -> You try both ( you need total amount of subsequences)
2. Dont pick
    - dp(i+1,j)

"""

from functools import lru_cache
class Solution:
    @cache
    def solve(self, i, j):
        # reached end of second string (total match)
        if j==len(self.t):
            return 1

        # first string exhausted
        if i==len(self.s):
            return 0

        # cur chars are same -> (1) pick (2) dont pick, hoping you have same char somewhere ahead
        if self.s[i] == self.t[j]:
            return self.solve(i+1, j+1) + self.solve(i+1,j)
        else: # move ahead, hoping you have needed char somewhere ahead
            return self.solve(i+1,j)
        
    def tabular_dp_reverse(self, s, t) -> int:
        ns, nt = len(s), len(t)
        dp = [[0 for _ in range(nt + 1)] for _ in range(ns + 1)]

        # Base case: If t is empty, there's exactly one way to match it (by choosing nothing)
        for i in range(ns + 1):
            dp[i][nt] = 1

        # Fill the DP table bottom-up
        for i in range(ns - 1, -1, -1):
            for j in range(nt - 1, -1, -1):
                if s[i] == t[j]:
                    # Either match the current character or skip it
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    # Skip the current character in `s`
                    dp[i][j] = dp[i + 1][j]

        # The result is stored in dp[0][0]
        return dp[0][0]

    def tabular_dp_incr(self, s, t) -> int:
        ns, nt = len(s), len(t)
        dp = [[0 for _ in range(nt + 1)] for _ in range(ns + 1)]

        # Base case: If t is empty, there's exactly one way to match it (by choosing nothing)
        for i in range(ns + 1):
            dp[i][0] = 1

        # Fill the DP table bottom-up
        for i in range(1, ns+1):
            for j in range(1, nt+1):
                if s[i-1] == t[j-1]:
                    # Either match the current character or skip it
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # Skip the current character in `s`
                    dp[i][j] = dp[i - 1][j]

        # The result is stored in dp[0][0]
        return dp[ns][nt]


    def numDistinct(self, s: str, t: str) -> int:
        self.s = s
        self.t = t

        return self.tabular_dp_incr(s,t)
        