"""
https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/?envType=daily-question&envId=2025-12-14
"""

from functools import lru_cache
MOD = 1_000_000_007

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        arr = list(corridor).copy()
        n = len(arr)

        @lru_cache(maxsize=1000)
        def solve(i: int, seats: int) -> int:
            # print(i, nseats)
            if i==n:
                return 1 if seats == 2 else 0

            # If the current section has exactly 2 "S"
            if seats == 2:
                # If the current element is "S", then we have to close the
                # section and start a new section from this index. Next index
                # will have one "S" in the current section
                if arr[i] == "S":
                    result = solve(i + 1, 1)
                else:
                    # If the current element is "P", then we have two options
                    # 1. Close the section and start a new section from this index
                    # 2. Keep growing the section
                    result = (solve(i + 1, 0) + solve(i + 1, 2)) % MOD
            else:
                # Keep growing the section. Increment "seats" if present
                # element is "S"
                if arr[i] == "S":
                    result = solve(i + 1, seats + 1)
                else:
                    result = solve(i + 1, seats)
            
            return result

        return solve(0,0)
