"""
PROBLEM: Number of paths to go from (0,0) to (nr,nc) i.e FIRST CELL -> LAST CELL
You can only move Right or Bottom by 1-Cell

2X2 => 2 ways
3X3 => 6 ways

ASSUMPTION: To make it easier for us we make some changes
1. We count ways to reacg Last -> First (will be same as first -> last)
2. You can move Top or Left by 1 Cell

SOLUTION:
- Each cell in dp[i][j] = no of ways to reach (0,0) from arr[i][j]
- DP Iterations (i->0,nr, j->0->nc)
    1. dp[0][0] = 1 #1 way to reach 0,0 from 0,0
    2. dp[0][j] or dp[i][0] = 1 
        - if you are in top row then you can only move left and reach 0,0
        - if you in left-most col, then you can only move up and reach 0,0
    3. Else, dp[i][j] = n(move_top) + n(move_left) =  dp[i-1][j] + dp[i][j-1]
- Return last cell of dp is answer

2X2
[1, 1]
[1, 2]

3X3
[1, 1, 1]
[1, 2, 3]
[1, 3, 6]

How to not make our reverse observations:
- Start iterations at (nr, nc) and that would be 1 (base condition)
- Iterate back in reverse (last cell -> first cell)
- Your edge/blocked edges change 
"""

def count_paths(nr, nc):
    dp = [[0 for _ in range(nc)] for _ in range(nr)]
    # dp[0][0] = 1
    for i in range(nr):
        for j in range(nc):
            if i==0 and j==0: # base 
                dp[i][j] = 1
            elif i==0 or j==0: # reached one edge
                dp[i][j] = 1
            else: # you can move both left and up
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    print(*dp, sep="\n")
    return dp[nr-1][nc-1]
    
def count_paths_no_assumption(nr, nc):
    dp = [[0 for _ in range(nc)] for _ in range(nr)]
    # dp[0][0] = 1
    for i in reversed(range(nr)):
        for j in reversed(range(nc)):
            if i==nr-1 and j==nc-1:
                dp[i][j] = 1
            elif i==nr-1 or j==nc-1:
                dp[i][j] = 1
            else: # you can move both left and up
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
    
    print(*dp, sep="\n")
    return dp[0][0]

    

count_paths(2,2) # 6
count_paths(3,3) # 6