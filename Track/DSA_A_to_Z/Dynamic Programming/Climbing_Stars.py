from os import *
from sys import *
from collections import *
from math import *

def countDistinctWays(n: int) -> int:
    """
    dp[i] = no of ways to reach 0 (REVERSED FROM PROBLEM STATEMENT)
    num ways from `n` -> 0 === num ways to reach 0 -> `n`
    """
    if n == 0:
        return 1
    elif n < 2:
        return n

    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2

    for i in range(2,n):
        dp[i] = (dp[i-1]+dp[i-2]) % 1000000007
 

    return dp[-1]