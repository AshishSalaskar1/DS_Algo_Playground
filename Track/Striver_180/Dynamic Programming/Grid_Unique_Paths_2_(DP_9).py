"""
Problem: Same as find all paths, but here you can be blocked by -1

Solution: 
 - If you are in first row, you can only move left. But that left can also be blocked, so dp[i][j] = dp[i][j-1]
 - If you are in first col, you can only move up. But that upper can also be blocked, so dp[i][j] = dp[i-1][j]
 - If arr[i][j] = -1, there can be no paths from here => dp[i][j] = 0
"""


def mazeObstacles(nr, nc, arr):
    dp = [[0 for _ in range(nc)] for _ in range(nr)]


    for i in range(nr):
        for j in range(nc):
            if i==0 and j==0: # base case
                dp[i][j] = 1
            elif arr[i][j] == -1: # you cant visit this cell
                dp[i][j] = 0
            elif i==0: # first row -> see if u can visit left and reach cell
                dp[i][j] = dp[i][j-1]
            elif j==0: # first col -> see if u can visit upper cell and reach start
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] += (dp[i-1][j]+dp[i][j-1]) % ((10**9)+7)
    
 
    return dp[-1][-1]