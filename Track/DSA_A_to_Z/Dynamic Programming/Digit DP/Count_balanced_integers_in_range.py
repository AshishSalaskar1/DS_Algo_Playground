"""
https://leetcode.com/problems/number-of-balanced-integers-in-a-range/
"""
from functools import cache

class Solution:
    def get_ways(self, r: str):
        n = len(r)

        @cache
        def solve(index: int, bound: bool, length: int, diff: int):
            if index == n:
                return 1 if length >= 2 and diff == 0 else 0

            ans = 0
            maxd = int(r[index]) if bound else 9

            for d in range(maxd + 1):
                newbound = bound and (d == maxd)

                if length == 0 and d == 0:
                    # still leading zeros
                    ans += solve(index + 1, newbound, 0, diff)
                else:
                    # alternating sum based on position
                    newdiff = diff + d if length % 2 == 0 else diff - d
                    ans += solve(
                        index + 1,
                        newbound,
                        length + 1,
                        newdiff
                    )

            return ans

        return solve(0, True, 0, 0)

    def countBalanced(self, low: int, high: int) -> int:
        return self.get_ways(str(high)) - self.get_ways(str(low - 1))
