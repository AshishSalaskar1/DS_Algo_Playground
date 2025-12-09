"""
https://leetcode.com/problems/count-special-triplets/description/?envType=daily-question&envId=2025-12-09
"""
from collections import defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        pos = defaultdict(list)

        # Store indices for each value
        for i, x in enumerate(nums):
            pos[x].append(i)

        res = 0

        # Treat j as the middle index
        for j, x in enumerate(nums):
            target = 2 * x
            if target not in pos:
                continue

            idxs = pos[target]  # sorted list of indices with value target

            # i < j
            left = bisect_left(idxs, j)               # indices strictly before j
            # k > j
            right = len(idxs) - bisect_right(idxs, j) # indices strictly after j

            res += (left * right)
            res = res%((10**9)+7)

        return res
