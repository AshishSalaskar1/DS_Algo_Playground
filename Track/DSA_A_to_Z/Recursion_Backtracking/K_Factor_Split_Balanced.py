"""
Link: https://leetcode.com/problems/balanced-k-factor-decomposition/

SOLUTION:
- Brute Force backtracking trying out all possibilities
"""

import math
from typing import List

class Solution:
    def solve(self, cur, count, idx):
        if count == 0:
            if cur == 1:
                cur_diff = max(self.curr) - min(self.curr)
                if cur_diff < self.best_diff:
                    self.best_diff = cur_diff
                    self.res = self.curr.copy()
            return
        
        for i in range(idx, len(self.divs)):
            factor = self.divs[i]
            if cur % factor == 0:
                self.curr.append(factor)
                self.solve(cur // factor, count - 1, i)
                self.curr.pop()

    def minDifference(self, n: int, k: int) -> List[int]:
        divs = [x for x in range(1,n) if n%x==0]
        self.divs = divs  # sort for consistent order

        self.curr = []
        self.res = []
        self.best_diff = float("inf")

        self.solve(n, k, 0)

        return self.res
