"""
PROBLEM: You are given ‘n’ items with certain ‘profit’ and ‘weight’ and a knapsack with weight capacity ‘w’.
You need to fill the knapsack with the items in such a way that you get the maximum profit. You are allowed to take one item multiple times.


SOLUTION:
- DP[i][j] -> max profit you can make using first `i` items with bag of max cap : `j`
- If j==0, you cant pick any ele
- if i==0, you can only pick first ele `x` times if its a multiple
- if weight[i] > j: You can pick curr element since its greater than available capacity
- if weight[i] <=j: 
    1. Dont pick curr element (j remains same)
    2. Pick this element and you can pick it up again (j = j-weights[i])
"""
from typing import List

def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    dp = [[0 for _ in range(w+1)] for _ in range(n)]

    for i in range(n):
        for j in range(w+1):
            if j==0:
                dp[i][j] = 0
            elif i==0: # only first element is left
                if j % weight[i] == 0: # you can pick this
                    dp[i][j] =  (j//weight[0]) * profit[0] # pick as many as you can
            elif weight[i] > j: # weight of curr ele is more
                dp[i][j] = dp[i-1][j]
            else: # either pick+pick again, dont pick current
                dp[i][j] = max(dp[i-1][j], profit[i]+dp[i][j-weight[i]])
    

    return dp[-1][-1]