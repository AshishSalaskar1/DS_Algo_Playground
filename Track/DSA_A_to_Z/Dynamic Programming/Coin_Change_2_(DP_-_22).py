"""
You are given an infinite supply of coins of each of denominations D = {D0, D1, D2, D3, ...... Dn-1}.
 You need to figure out the total number of ways W, in which you can make a change for value V using coins of denominations from D. 
 Print 0, if a change isn't possibl3


GREEDY WONT WORK
- Try for [1,2,3] Target=4
- Reason: It considers each combination as unique
    - [1,1,2], [1,2,1], [2,1,1] are different combinations buts still ONE WAY of picking

SOLUTION:
- dp[i][j] = num ways you can make target `j` using first `i`
- if j==0: You can not pick anything n make target=1
- if 1==0: You can pick only first coin (BUT, you can pick it INF times also)
- if coins[i] > j: You can pick curr coin
- else:
    1. Pick curr coin and then again pick same - dp[i][j-coins[i]]
    2. Dont pick curr coin  = dp[i-1][j]
"""

def countWaysToMakeChange(coins, target) :
    n = len(coins)
    dp = [[0 for _ in range(target+1)] for _ in range(n)]

    for i in range(n):
        for j in range(target+1):
            if j==0:
                dp[i][j] = 1
            elif i==0: # only first coint you can pick INF times
                dp[i][j] = 1 if j%coins[0] ==0 else 0
            elif coins[i] > j:
                dp[i][j] = dp[i-1][j]
            else:# you can NOT PICK, PICK (AND THEN REPICK AGAIN)
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

    return dp[-1][-1]



# GREEDY WAY
# def countWaysToMakeChange(coins, target) :
#     n = len(coins)
#     coins = sorted(coins)
#     dp = [-1 for _ in range(target+1)]

#     dp[0] = 1

#     for cur_target in range(1, target+1):
#         ways_from_here = 0
#         for coin in coins:
#             if coin > cur_target:
#                 break
#             else:
#                 # check if you can make cur_target - coin
#                 if dp[cur_target-coin]  != -1:
#                     ways_from_here += dp[cur_target-coin]
        
#         if ways_from_here > 0:
#             dp[cur_target] = ways_from_here
#         print(cur_target, ways_from_here)

#     print(dp)
#     return 0 if dp[-2] == -1 else dp[-2]

    
































#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))