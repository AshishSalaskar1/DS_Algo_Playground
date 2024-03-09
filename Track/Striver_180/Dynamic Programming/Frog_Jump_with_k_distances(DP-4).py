"""
Frog jump but you are given `k`, you can 1 to k places from `i`
Each jump from i -> j needs abs(arr[i], arr[j]) energy

Solution
- Reverse, min cost to go from last to first index. You jump back instead of ahead
- From `i` you can jump i-1,i-2 ... i-k
    - dp[i] -> min energy needed to reach from last to 0
    - dp[0] = 0, you have already reached first -> abs(arr[i]-arr[i])=0
    - When u jump back from i to jump_index,
        1. You need energy to jump from jump_index <- i |GIVEN BY ABS(....)|
        2. Plus from 0 <- jump_index you need energy |MIN STORED IN dp array|
"""

# REACH FIRST FROM LAST
def minimizeCost(n : int, k : int, arr : List[int]) -> int:
    dp = [float("inf") for _ in range(n)]
    
    # you already reached first
    dp[0] = 0
    for i in range(1, n):
        min_steps = float("inf")

        for step_size in range(1,k+1):
            jumped_index = i-step_size

            # dont worry <0, because <0 means atleast once you have reached 0
            if jumped_index >= 0:
                # if u jump to non-first, you need abs() energy to jump + jump from there to start
                min_steps = min(dp[jumped_index] + abs(arr[i]-arr[jumped_index]) ,min_steps)

        dp[i] = min_steps

    return dp[-1]