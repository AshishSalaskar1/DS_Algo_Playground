""""
PROBLEM: 
Your task is to count the number of ways to construct sum n by throwing a dice one or more times. Each throw produces an outcome between 1 and  6.
For example, if n=3, there are 4 ways:

1+1+1
1+2
2+1
3

SOLUTION:
1. Recursive
- if n<0: return 0
- if n==0: return 1 (you have made up SUM = N)
- Else try all dice rolls (1 = min(n,6))

2. Tabulations
dp[0] = 1 # there is one way to make sum = 0 (by not throwing)
- For each i: 1->n
    -dp[i] += (dp[i-6] ...+.. dp[i-1])
 """
import sys


# def solve(n):
#     if n<0:
#         return 0
    
#     if n==0:
#         return 1

#     ways = 0
#     for x in range(1,min(6,n)+1):
#         ways += solve(n-x)

#     return ways

n = int(sys.stdin.readline())

dp = [0]*(n+1)
dp[0] = 1 # there is one way to make sum = 0 (by not throwing)


for i in range(1,n+1):
    for dice_roll in range(1,min(6,i)+1): 
        dp[i] = (dp[i] + dp[i-dice_roll]) % (10**9+7)


print(dp[-1])