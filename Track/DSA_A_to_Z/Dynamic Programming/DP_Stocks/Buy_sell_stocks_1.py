"""
PROBLEM:
- You are given an array prices where prices[i] is the price of a given stock on the ith day.
- You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

SOLUTION
- You can only buy and sell ONCE
- For each day, pick smallest value you could have picked in earlier days <= MAX of this is most profitable
- OR find (i,j) such that arr[j]-arr[i] is maximized (for this arr[i] needs to be as small as possible and arr[j] as big as possible)

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_till_now = prices[0]
        res = 0
        for x in prices[1:]:
            res = max(res, x-min_till_now)
            min_till_now = min(min_till_now, x)
        
        return res
        