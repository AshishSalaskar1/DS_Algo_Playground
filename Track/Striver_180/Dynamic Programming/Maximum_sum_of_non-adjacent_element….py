from sys import stdin

def maximumNonAdjacentSum(arr):
    n = len(arr)
    
    if n == 1:
        return arr[0]
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    dp[1] = max(arr[1], arr[0])

    for i in range(2,n):
        dp[i] = max(dp[i-1], arr[i]+dp[i-2])
        
    return dp[n-1]

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1