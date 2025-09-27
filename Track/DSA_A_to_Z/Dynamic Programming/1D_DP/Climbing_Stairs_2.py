"""
Link: https://leetcode.com/contest/biweekly-contest-166/problems/climbing-stairs-ii/description/

"""
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float("inf")]*(n+1)

        dp[-1] = 0

        for i in range(n-1, -1, -1):
            for step in range(1,4):
                j = i+step
                if j>n: break
                dp[i] = min(dp[i], costs[j-1] + (j-i)**2 + dp[j])

        return dp[0]
        