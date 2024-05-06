"""
SAME as BUY_SELL_STOCK_2 and BUY_SELL_WITH_COOLDOWN
- Here you can do as many buy/sell possibles, 
- But, for each sell you make you are charged some fees (same for all stocks -> broker fees)
    - Fees is charged on each (buy,sell) transaction only

"""

class Solution:
    def solve(self, cur_day, buy):
        idx = (cur_day, buy)

        if idx in self.dp: 
            return self.dp[idx]

        if cur_day >= self.n: # days exhausted
            res = 0
        else: # normal day
            if buy == 1: # you can buy
                res =  max(
                    self.solve(cur_day+1, buy=1),
                    -self.arr[cur_day] + self.solve(cur_day+1, buy=0)
                )
            else: # you can sell -> SELL means you need to pay transaction fees
                res =  max(
                    self.solve(cur_day+1, buy=0),
                    -self.fee + self.arr[cur_day] + self.solve(cur_day+1, buy=1)
                )
        
        self.dp[idx] =res
        return res

    def maxProfit(self, prices: List[int], fee: int) -> int:
        self.arr = prices
        self.n = len(prices)
        self.fee = fee
        self.dp = {}
        return self.solve(0, buy=1)
        