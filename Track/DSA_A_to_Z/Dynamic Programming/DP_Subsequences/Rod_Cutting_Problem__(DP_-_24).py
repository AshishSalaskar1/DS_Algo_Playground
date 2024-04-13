from sys import stdin
import sys

dp = {}

# max profit that you can make by cutting into rods of length (cur_idx+1)
def cutRod(cur_idx, rem_rod_length, prices):

    dp_idx = (cur_idx, rem_rod_length)

    if dp_idx in dp:
        return dp[dp_idx]

    if cur_idx==0: # only 1 element is remaining -> you can pick it INF times
        dp[dp_idx] =  prices[0] * rem_rod_length
        return  dp[dp_idx]

    # dont cut 
    dont_pick = 0 + cutRod(cur_idx-1, rem_rod_length, prices)

    # CUT -> cur_rod_len = idx+1 (1 based indexing)
    cur_rod_len = cur_idx+1
    # Can you cut or not
    if cur_rod_len <= rem_rod_length:
        pick = price[cur_idx] + cutRod(cur_idx, rem_rod_length-cur_rod_len, prices)
        dp[dp_idx] =  max(dont_pick, pick)
    else:
        dp[dp_idx] =  dont_pick

    return  dp[dp_idx]
    


# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    dp = {} # RESET DP ARRAY EACH TIME
    print(cutRod(n-1, n, price))
    t = t-1