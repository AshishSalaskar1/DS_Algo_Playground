"""
Problem: Given nxm matrix find number of ways you can reach (0,0) -> (n,m) 
You can only move right or down

Reverse: 
    - (0,0) <- (n,m) 
    - You can move up and left
    - You can keep same but then u need to traverse reverse for DP

Solution:
    - dp[i][j] = num ways you can reach (0,0) from row:i and col:j
    - If you are in first row, you can reach start in only 1 way (move left always)
    - If you are in first col, you can reach start in only 1 way (move up always)
"""
def uniquePaths(nr, nc):
    dp = [[0 for _ in range(nc)] for _ in range(nr)]


    for i in range(nr):
        for j in range(nc):
            if i==0 and j==0: # base case
                dp[i][j] = 1
            if i==0: # you are at first row
                dp[i][j] = 1
            elif j==0: # you are at first column
                dp[i][j] = 1
            else: # you can move 2 ways
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # print(dp)
    return dp[-1][-1]