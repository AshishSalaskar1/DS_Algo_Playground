"""
dp[i][j] = min effort needed to reach (0,0) <- (n,m)
"""

def minSumPath(arr):
    nr = len(arr)
    nc = len(arr[0])
    dp = [[float("inf") for _ in range(nc)] for _ in range(nr)]

    for i in range(nr):
        for j in range(nc):
            if i==0 and j==0: # you reached 0,0
                dp[i][j] = arr[i][j]
            elif i==0: # first row, only move left
                dp[i][j] = arr[i][j] + dp[i][j-1]
            elif j==0: # first col, only move up
                dp[i][j] = arr[i][j] + dp[i-1][j]
            else: # two options available
                dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]