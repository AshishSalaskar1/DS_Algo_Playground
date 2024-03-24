"""
You can rob adjacent houses, but first and last houses are considered to be adjacent

Solution:
- Max of house_rob(exclude_last_house), house_rob(exclude_first_house)


Here,
    - dp[i] = max u can make by robbing till house [i]
    - You can rob current + leave curr-1, leave this + rob curr-1 
"""

def dp_maximumNonAdjacentSum(arr):
    n = len(arr)

    if n==1:
        return arr[0]
    elif n==2:
        return max(arr[0],arr[1])

    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2,n):
        dp[i] = max(arr[i]+dp[i-2], dp[i-1])
    
    return dp[-1]

def houseRobber(arr):
    if len(arr)==1:
        return arr[0]

    return max(
        dp_maximumNonAdjacentSum(arr[1:]),
        dp_maximumNonAdjacentSum(arr[:-1])
    )