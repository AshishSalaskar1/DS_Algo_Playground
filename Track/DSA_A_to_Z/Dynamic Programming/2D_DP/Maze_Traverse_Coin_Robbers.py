"""
Problem: Maximum Amount of Money Robot Can Earn
- Similar to Witcher II problem, at each point you have certain values (+ -> you can pick coins, - -> you lose to robbers)
- You can avoid at max 2 coin-robbers in the total traversal
- You need to reach (nr,nc) from (0,0) and give max profit
- IMP: Max profit can be negative also

[0, 1,-1]
[1,-2, 3]
[2,-3, 4]

OP: 8 | (0,0) -> (0,1) -> (1,1) avoid getting robbed -> (1,2) -> (2,2)

==> SOLUTION:
Base Cases:
1. Anything outside bounds = float("inf") | You cant take this path
2. If you are at (nr,nr):
    - if coins[nr-1][nr-1] is negative? You will lose coins[nr-1][nc-1] in case escapes left = 0, else you will not lose anything
    - if positive, take it as is
3. At each point (i,j,escapes_left)
    1. if coins[i][j]<0 and escapes_left>0:
        - You WILL NOT ALWAYS ESCAPE IF POSSIBLE (since you have limited escapes you may want to escape later bigger coin robbers)
        - In base case -> LAST CELL -> YOU WILL ALWAYS ESCAPE IF POSSIBLE (nothing in future to escape)
        - max(
            0 + self.solve(i+1, j, escapes_left-1),
            0 + self.solve(i, j+1, escapes_left-1),
            self.coins[i][j] + self.solve(i+1, j, escapes_left),
            self.coins[i][j] + self.solve(i, j+1, escapes_left)
        )
    2. If coins[i][j] > 0 -> you will always pick it and move
        - max(
            self.coins[i][j] + self.solve(i+1, j, escapes_left),
            self.coins[i][j] + self.solve(i, j+1, escapes_left)
        )
"""
 

from functools import lru_cache, cache
class Solution:
    @cache
    def solve(self, i, j, escapes_left):
        if i>=self.nr or j>=self.nc:
            return float("-inf")

        if i==self.nr-1 and j==self.nc-1:
            if self.coins[i][j] < 0:
                return 0 if escapes_left>0 else self.coins[i][j]
            else:
                return self.coins[i][j]
        
        ans = float("-inf")
        if self.coins[i][j] < 0 and escapes_left > 0:
            return max(
                self.solve(i+1,j, escapes_left-1),
                self.solve(i,j+1, escapes_left-1),
                self.coins[i][j] + self.solve(i+1,j, escapes_left-1),
                self.coins[i][j] + self.solve(i,j+1, escapes_left-1)
            )
        else:
            return max(
                    self.coins[i][j] + self.solve(i+1,j, escapes_left),
                    self.coins[i][j] + self.solve(i,j+1, escapes_left)
                )

    def solve_tabulation(self, arr, nr, nc, escapes=2):
        # Initialize DP table with size (nr+1) x (nc+1) x (escapes+1)
        dp = [[[float("-inf") for _ in range(escapes + 1)] for _ in range(nc + 1)] for _ in range(nr + 1)]

        # Base case: Bottom-right cell
        for k in range(escapes + 1):
            if arr[nr - 1][nc - 1] < 0 and k > 0:
                dp[nr - 1][nc - 1][k] = 0  # Use an attack
            else:
                dp[nr - 1][nc - 1][k] = arr[nr - 1][nc - 1]

        # Fill DP table bottom-up
        for i in range(nr - 1, -1, -1):
            for j in range(nc - 1, -1, -1):
                for k in range(escapes, -1, -1):
                    if i == nr - 1 and j == nc - 1:
                        continue  # Skip bottom-right cell (already initialized)

                    if arr[i][j] < 0 and k > 0:  # Use an attack
                        dp[i][j][k] = max(
                            arr[i][j] + dp[i][j + 1][k],
                            arr[i][j] + dp[i + 1][j][k],
                            dp[i][j + 1][k - 1],
                            dp[i + 1][j][k - 1],
                        )
                    else:
                        dp[i][j][k] = max(
                            arr[i][j] + dp[i][j + 1][k],
                            arr[i][j] + dp[i + 1][j][k],
                        )

        # Result is the max amount starting at the top-left with `escapes` left
        return max(dp[0][0])
 

    def maximumAmount(self, coins: List[List[int]]) -> int:
        self.nr, self.nc = len(coins), len(coins[0])
        self.coins = coins

        return self.solve_tabulation(coins, self.nr, self.nc, 2)