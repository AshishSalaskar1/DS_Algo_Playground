"""
https://www.naukri.com/code360/problems/tiling-problem_630464

You have been given a board where there are '2' rows and 'N' columns. You have an infinite supply of 2x1 tiles, and you can place a tile in the following ways:

1. Horizontally as 1x2 tile
2. Vertically as 2x1 tile
Count the number of ways to tile the given board using the available tiles.

SOLUTION:
DP[i] = number of ways you can fill a board with `i` columns
dp[0] = 1 # how many ways can you tile with 0 columns = 1
dp[1] = 1 # 1-vertically placed tile
dp[2] = 2 # 2-vert tile OR 2 horizontal tiles 



"""
def numberOfWaysToTile(n):
    dp = [0]*(n+1)
    dp[0] = 1 
    dp[1] = 1 # |
    dp[2] = 2 # || or =

    MOD  = (10**9)+7
    if n < 2:
        return dp[n]

    for i in range(3,n+1):
        # OPTION 1: 2x1 vertical tile
        #    - Place a vertical tile here -> then possible ways = dp[i-1]
        # OPTION 2: 2 1x2 horizontal tiles
        #   💡 Think that whatever tile you place ends at `i`. That means a 2x2 tile will also eat up one place before `i`
        #    - Place 2 horizontail tiles here -> this will eat up current place+place before this = hence dp[i-1]
        dp[i] = (dp[i-1]+dp[i-2])%MOD

    return dp[n]

