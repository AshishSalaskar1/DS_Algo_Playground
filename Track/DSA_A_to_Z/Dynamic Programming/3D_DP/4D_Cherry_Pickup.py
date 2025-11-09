"""
PROBLEM: https://leetcode.com/problems/cherry-pickup/

SOLUTION 1: ( DOESNT WORK )
1. Best path from (0,0) -> (n,n)
2. Using DP array send the path too
3. Make all berries in the path taken as 0
4. Repeat (1) again


SOLUTION 2:
- Going from (0,0) -> (n,n) and then (0,0) <- (n,n) is same as 2 ppl simulataneously going from (0,0) -> (n,n)
- If both ppl reach same cell, only 1 can take it (This simulates one path has already pickedup so second path cant pick up)
"""

from typing import List
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dp(r1, c1, r2, c2):
            # Calculate c2 and r2 from steps if needed (in 3D version)
            # But in 4D version we pass everything directly.

            # Out of bounds or thorn
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or \
               grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float('inf')

            # If both reach the bottom-right cell
            if r1 == c1 == r2 == c2 == n - 1:
                return grid[r1][c1]

            cherries = 0
            if r1 == r2 and c1 == c2:
                cherries += grid[r1][c1]  # Only count once if same cell
            else:
                cherries += grid[r1][c1] + grid[r2][c2]

            # Try all 4 combinations of moves (down or right)
            next_max = max(
                dp(r1 + 1, c1, r2 + 1, c2),  # down, down
                dp(r1 + 1, c1, r2, c2 + 1),  # down, right
                dp(r1, c1 + 1, r2 + 1, c2),  # right, down
                dp(r1, c1 + 1, r2, c2 + 1)   # right, right
            )

            cherries += next_max
            return cherries

        result = dp(0, 0, 0, 0)
        return max(0, result)
