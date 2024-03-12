"""
Problem: Find subset in array such that sum = target, return if its possible or not

Solution:
- DP : 
    - rows (0 -> n)
    - cols (0, target+1)
    - dp[row][col] -> can you make target=col using first `row` elements (You can make use of all or some you need)
"""

def subsetSumToK(n, k, arr):
    dp = [[False for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        for j in range(k+1):
            if j==0: # to make 0 target -> dont pick anything 
                dp[i][j] = True
            elif i==0: # you have only first element (1 coin)
                dp[i][j] = True if j==arr[i] else False
            elif arr[i] > j: # you cant pick current one (curr > needed_target)
                dp[i][j] = dp[i-1][j]
            else: # you can either pick this one or ignore
                dp[i][j] = dp[i-1][j-arr[i]] or dp[i-1][j]
    
    return dp[-1][-1]