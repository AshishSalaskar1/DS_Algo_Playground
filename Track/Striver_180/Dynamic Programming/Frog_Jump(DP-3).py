from typing import *

  
def frogJump(n: int, arr: List[int]) -> int:
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = abs(arr[1]-arr[0])
    for i in range(2,n):
        dp[i] = min(dp[i-1]+abs(arr[i]-arr[i-1]), dp[i-2]+abs(arr[i]-arr[i-2]))     
#     print(dp)
    return dp[n-1]