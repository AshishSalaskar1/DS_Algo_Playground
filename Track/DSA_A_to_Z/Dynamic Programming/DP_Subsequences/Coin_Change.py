"""
Problem: https://leetcode.com/problems/coin-change/
Good Video: https://www.youtube.com/watch?v=NNcN5X1wsaw


IDEATION:
- dp[i] = min coins needed to make amount `i`
- 💡DONT THINK WHY NOT TAKING SAME TWICE ( that gets auto handled )
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0 # dp[i] = min coins needed to make amount `i`

        for cur_amount in range(1,amount+1):
            for coin in coins:
                if coin > cur_amount: break

                rem = cur_amount - coin
                if dp[rem] != float("inf"):
                    dp[cur_amount] = min(dp[cur_amount], 1+dp[rem])
        
        return dp[amount] if dp[amount] != float('inf') else -1


        