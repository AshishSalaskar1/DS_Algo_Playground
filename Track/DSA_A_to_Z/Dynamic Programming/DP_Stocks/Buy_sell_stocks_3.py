"""
BUY AND SELL STOCK - III
BUY AND SELL STOCK:
I -> only buy and sell once
II -> buy and sell as many times as needed
III -> buy and sell at most twice (2 transactions)
IV -> buy and sell at most k times (k transactions)

- One transaction: BUY -> SELL

"""

class Solution:
    def solve(self, cur_day, buy, ntransactions):
        idx = (cur_day, buy, ntransactions)

        if idx in self.dp:
            return self.dp[idx]

            
        if ntransactions >= 2: # 2 transactions have already been done
            res = 0
        elif cur_day >= self.n: # after days are over you cant do anything (even if have bought but unsold - ignore)
            res = 0
        elif buy == 1: # you can BUY
            res = max(
                self.solve(cur_day+1, 1, ntransactions),
                -self.arr[cur_day]+self.solve(cur_day+1, 0, ntransactions)
            )
        else: # you can SELL -> completes one transaction
            res = max(
                self.solve(cur_day+1, 0, ntransactions),
                self.arr[cur_day]+self.solve(cur_day+1, 1, ntransactions+1)
            )

        self.dp[idx] = res
        return res
        

    def maxProfit(self, prices: List[int]) -> int:
        self.arr = prices
        self.n = len(prices)
        self.dp = {}

        # you can only buy on first day
        res = self.solve(0, buy=1, ntransactions=0)
        return res
        