"""
PROBLEM: Domino and Tromino Tiling
https://leetcode.com/problems/domino-and-tromino-tiling/?envType=study-plan-v2&envId=leetcode-75

SOLUTION:
- BEST EXPLAINATION: https://leetcode.com/problems/domino-and-tromino-tiling/solutions/1620975/c-python-simple-solution-w-images-explanation-optimization-from-brute-force-to-dp
(REFER POSSIBLE DIAGRAMS ONLY)
"""
from functools import cache
class Solution:
    @cache
    def fill_tiles(self, col: int, prev_gap: str) -> int:
        if col>self.n:
            return 0
        if col==self.n: # just after all cols are done (not exactly at last)
            return 0 if prev_gap else 1 # if still gaps are left -> this tiling patern is not valid
        if prev_gap: # previously gap was left
            return (
                self.fill_tiles(col+1, False) + # add tromino (U or D) -> will fill gap
                self.fill_tiles(col+1, True) # add a horizontal domino -> will create another gap in next
            ) % (10**9 + 7)
        else:
            return (
                self.fill_tiles(col+1, False) + # one vertical domino (takes 1 cols)
                self.fill_tiles(col+2, False) + # 2 horizontal domino (takes 2 cols)
                2*self.fill_tiles(col+2, True) # all tromino (takes 2 cols but leaves gap)
            ) % (10**9 + 7)

    def numTilings(self, n: int) -> int:
        self.n = n
        return self.fill_tiles(0, False) % (10**9 + 7)
        