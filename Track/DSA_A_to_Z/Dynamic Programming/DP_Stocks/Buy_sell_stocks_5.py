"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/?envType=daily-question&envId=2025-12-17

QUESTION:
- You are given prices array + max transactions `k` you can make
- You can buy/sell as many times as you want but at max `k` transactions
- Buy/Sell are of 2 types 
    1. long buy sell -> buy at `i` sell at `j` (j>i)
    2. short sell buy -> sell at `i` buy at `j` (j>i)
- You can only hold one position at a time (long/short)



MAIN LOGIC: 
- If you long buy -> you must long sell to close position
- If you short sell -> you must short buy to close position

So, can_buy wont work here, we need to track 3 states

State = 0 -> not holding anything
State = 1 -> holding a long pos
State = 2 -> holding a short pos
"""
from functools import lru_cache
class Solution:
    def maximumProfit(self, prices, k):
        n = len(prices)
        NEG = -10**18


        @lru_cache(maxsize=10000)
        def dfs(i, t, state):
            if i == n:
                return 0 if state == 0 else NEG

            # you dont do anything
            ans = dfs(i + 1, t, state)

            if state == 0: # you are not holding anything
                ans = max(ans, -prices[i] + dfs(i + 1, t, 1) ) # take a short position 
                ans = max(ans, +prices[i]+ dfs(i + 1, t, 2) ) # take a long position
            elif state == 1 and t < k: # you are holding long position -> can only sell
                ans = max(ans, dfs(i + 1, t + 1, 0) + prices[i])
            elif state == 2 and t < k: # you are holding short position -> can only sell
                ans = max(ans, dfs(i + 1, t + 1, 0) - prices[i])

            return ans

        return dfs(0, 0, 0)