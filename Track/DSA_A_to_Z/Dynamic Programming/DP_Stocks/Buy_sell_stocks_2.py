"""
PROBLEM: 
BUY AND SELL STOCK:
I -> only buy and sell once
II -> buy and sell as many times as needed
III -> buy and sell at most twice (2 transactions)
IV -> buy and sell at most k times (k transactions)

- You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
- On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
- Find and return the maximum profit you can achieve. 


RECURSIVE
- params: cur_day (cur trading day), buy (can you BUY/SELL)
1. If you BUY previously, now the only options are
    - Dont do anything
    - SELL the stock now (arr[cur] + fn(cur+1, SOLD))
2. If you SELL previously, now the only options are
    - Dont do anything
    - BUY the stock now (-arr[cur] + fn(cur+1, SOLD))

TABULATION
- REMEMBER AT the value of buy (its what you can do, NOT what you have previously done)
0 -> YOU CAN SELL (on the current day)
1 -> YOU CAN BUY (on the current day)

"""

class Solution:
    def fn(self, cur_day, buy):
        """
            0 -> YOU CAN SELL (on the current day)
            1 -> YOU CAN BUY (on the current day)
        """
        idx = (cur_day, buy)
        if idx in self.dp:
            return self.dp[idx]

        if cur_day >= self.n: # after days are over you cant do anything (even if have bought but unsold - ignore)
            self.dp[idx] = 0
        elif buy == 0: # You can SELL
            self.dp[idx] =  max(
                self.fn(cur_day+1, 0), # do nothing
                self.arr[cur_day] + self.fn(cur_day+1, buy=1) # SELL (+ve will offset previous buys)
        else: # You can BUY
            self.dp[idx] =  max(
                self.fn(cur_day+1, 1), # do nothing
                -self.arr[cur_day] + self.fn(cur_day+1, buy=0)  # BUY (-ve arr since buying is loss for now)
            )
            )
        
        return self.dp[idx]

        
    def maxProfitRecursive(self, arr: List[int]) -> int:
        n = len(arr)
        self.arr = arr
        self.n = n
        self.dp = {}

        return self.fn(0,buy=1) # You can only BUY on FIRST DAY
    
    # BOTTOM UP APPROACH
    def maxProfit(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float("-inf") for _ in range(2)] for _ in range(n+1)]

        dp[n][0] = dp[n][1] = 0 # exhausted the days for trading
        for cday in reversed(range(n)):
            for buy in range(2): 
                if buy==1: # you can buy
                    dp[cday][buy] = max(dp[cday+1][1], dp[cday+1][0]-arr[cday])
                else: # you can sell
                    dp[cday][buy] = max(dp[cday+1][0], dp[cday+1][1]+arr[cday])

        
        print(*dp, sep="\n")
        return dp[0][1] # you can only buy on first day


        

        