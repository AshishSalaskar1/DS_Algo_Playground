from functools import lru_cache
from typing import List
import sys

class Solution:
    MOD = 10**9 + 7

    def countStableSubsequences(self, nums: List[int]) -> int:
        # Work with parity only: 0 = even, 1 = odd
        arr = [x & 1 for x in nums]
        n = len(arr)

        @lru_cache()
        def solve(i: int, last: int, second_last: int) -> int:
            if i == n:
                return 1

            # Option 1: skip nums[i]
            res = solve(i + 1, last, second_last)

            # Option 2: pick nums[i] if it doesn't create 3 in a row with same parity
            cur = arr[i]
            if not (last == second_last == cur):
                res += solve(i + 1, cur, last)

            return res % self.MOD

        # Subtract 1 to exclude the empty subsequence
        return (solve(0, -1, -1) - 1) % self.MOD