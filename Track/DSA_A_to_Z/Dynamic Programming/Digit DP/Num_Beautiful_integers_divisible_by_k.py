"""
https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/submissions/1867823172/?envType=problem-list-v2&envId=2chw7ar7

Class Digit DP

## WHY THE REM = (REM*10+d) % K
- https://www.youtube.com/watch?v=yNKhlzYjDDs
- Seems to be mimicking how we do Division on paper
"""
from functools import cache

class Solution:
    def get_ways(self, r: str):
        n = len(r)

        @cache
        def solve(index, bound, isvalid, rem, evenCount, oddCount):
            if index == n:
                return isvalid and rem == 0 and evenCount == oddCount

            ans = 0
            maxd = int(r[index]) if bound else 9

            for d in range(maxd + 1):
                newbound = bound and (d == maxd)
                newisvalid = isvalid or (d != 0)

                if newisvalid:
                    newrem = (rem * 10 + d) % self.k
                    neven = evenCount + (d % 2 == 0)
                    nodd  = oddCount + (d % 2 == 1)
                else:
                    newrem = 0
                    neven = evenCount
                    nodd  = oddCount

                ans += solve(
                    index + 1,
                    newbound,
                    newisvalid,
                    newrem,
                    neven,
                    nodd
                )

            return ans

        return solve(0, True, False, 0, 0, 0)

    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        self.k = k
        return self.get_ways(str(high)) - self.get_ways(str(low - 1))
