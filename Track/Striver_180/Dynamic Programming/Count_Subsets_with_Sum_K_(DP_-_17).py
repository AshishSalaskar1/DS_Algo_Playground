from typing import List

def findWays(arr, target):
    n = len(arr)
    dp = [[0 for _ in range(target+1)] for _ in range(n)]

    for i in range(n):
        for j in range(target+1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 1 if arr[0] == j else 0
            elif arr[i] > j:
                dp[i][j] = dp[i-1][j] 
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i]]

    return dp[-1][-1] % ((10**9)+7)