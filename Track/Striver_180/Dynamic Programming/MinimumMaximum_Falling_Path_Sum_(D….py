"""
PROBLEM:
    - Given a matrix you need to go from row=0 -> last row (any point) with MAX SUM

SOLUTION:
- Reverse: Go from last row to first row maximizing sum
- dp[row][col] = max cost from (row,col) to any cell in first row
"""


def getMaxPathSum(arr):
    nr, nc = len(arr), len(arr[0])

    dp = [[float('-inf') for _ in range(nc)] for _ in range(nr)]
    # dp[0] = arr[0]

    for row in range(nr):
        for col in range(nc):
            if row==0: # first row 
                dp[row][col] = arr[row][col]
            else: # you have 3 options
                options = [(row-1,col-1), (row-1,col), (row-1,col+1)]
                for r,c in options:
                    if r>=0 and c>=0 and r<nr and c<nc:
                        dp[row][col] =max(dp[r][c] + arr[row][col], dp[row][col])
    
    return max(dp[-1])

























#   taking inpit using fast I/O
def takeInput() :
    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix=[list(map(int, stdin.readline().strip().split(" "))) for row in range(n)]

    return matrix, n, m


#   main
T = int(input())
while (T > 0):
    T -= 1
    matrix, n, m = takeInput()
    print(getMaxPathSum(matrix))