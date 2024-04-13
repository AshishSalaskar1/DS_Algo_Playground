"""
Problem: Given [weight] and [costs] and W. 
- Give max profit you can earn by picking elements with total weight<=W.
- Bounded: You can pick one element only once


SOLUTION
- dp[i][j] -> max profit you can earn by picking upto `i` elements and  W=`j`
- j==0 -> dp[i][j] = 0 (W=0, you cant pick anything)
- i==0 (Only first ele is available )
- If weight[i] > j = dp[i-1][j] ==> You cant pick ele i since it wont fit in bag 
- Else: 
    - Max of 2 options
    1. Pick curr ele `i`: dp[i-1][j-weights[i]] + cost[i]
    2. Dont pick: dp[i-1][j]
"""


def zero_one_knapsack(weights, costs, w):
    n = len(weights)

    dp = [[0 for _ in range(w+1)] for _ in range(n) ]

    for i in range(n):
        for j in range(w+1):
            if i==0:
                dp[i][j] = costs[0] if weights[0]<=j else 0
            elif weights[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], costs[i] + dp[i-1][j-weights[i]])

    return dp[-1][-1]


N = int(input())
for _ in range(N):
    n = int(input())
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    w = int(input())
    print(zero_one_knapsack(weights, costs, w))