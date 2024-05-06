"""
Similar to BUY_SELL_STOCK_2 (can sell any number of times)
Plus: There is cooldown next day after you sell

RECURSION PARAMS
1. cur_day -> present day
2. buy -> can you BUY(1) or SELL(0) the stocks on cur_day
3. cooldown -> is this day a cooldown day
    True -> cooldown -> you can only ignore
    False -> You can buy/sell as usual (max[nothing, buy, sell])
    - In case you sell, next day cooldown=True
"""

class Solution:
    def solve(self, cur_day, buy, cooldown):
        """
        buy = 1(you can buy), 0(you can sell)
        cooldown = True(you can buy/sell), False(you can buy/sell)
        """
        idx = (cur_day, buy, cooldown)

        if idx in self.dp: 
            return self.dp[idx]

        if cur_day >= self.n: # days exhausted
            res = 0
        elif cooldown is True: # cur day is cooldown (you cant buy/sell)
            res =  self.solve(cur_day+1, buy, cooldown=False)
        else: # normal day
            if buy == 1: # you can buy
                res =  max(
                    self.solve(cur_day+1, buy=1, cooldown=False),
                    -self.arr[cur_day] + self.solve(cur_day+1, buy=0, cooldown=False)
                )
            else: # you can sell -> SELL means cooldown next day
                res =  max(
                    self.solve(cur_day+1, buy=0, cooldown=False),
                    self.arr[cur_day] + self.solve(cur_day+1, buy=1, cooldown=True)
                )
        
        self.dp[idx] = res
        return res


    def maxProfit(self, prices: List[int]) -> int:
        self.arr = prices
        self.n = len(prices)
        self.dp = {}
        return self.solve(0, buy=1, cooldown=False)
        