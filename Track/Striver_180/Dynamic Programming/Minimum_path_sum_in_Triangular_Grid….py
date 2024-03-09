"""
PROBLEM:
1
2,3
3,6,7
8,9,6,10

Given such triange, from arr[row][col] -> arr[row+1][col], arr[row+1][col+1]
Find min cost path from first to last row (You can reach any ele in last row)


SOLUTION:
- REVERSE: 
    - Reach from any ele in last row to first row -> MIN COST PATH
    - arr[row-1][col-1], arr[row-1][col] <- arr[row][col]

- dp[row][col] = min cost to reach from [row][col] to first row
- IMP: dp = [[0 for _ in range(x+1)] for x in range(n)]
- For each iteration check if both options are available or not
"""

def minimumPathSum(arr, n):
    # print(arr)
    dp = [[0 for _ in range(x+1)] for x in range(n)]
    
    dp[0] = arr[0]
    
    for row in range(1,n):
        prev_row_len = len(dp[row-1])
        for col in range(row+1):
            opt1 = col
            opt2 = col-1
            min_price = float('inf')

            if opt1<prev_row_len and opt1>=0:
                min_price = min(min_price, dp[row-1][opt1])

            if opt2<prev_row_len and opt2>=0:
                min_price = min(min_price, dp[row-1][opt2])
            
            dp[row][col] = min_price + arr[row][col]
    
    return min(dp[-1])