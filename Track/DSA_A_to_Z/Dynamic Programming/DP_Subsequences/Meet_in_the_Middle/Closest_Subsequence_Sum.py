"""
Closest Subsequence Sum: https://leetcode.com/problems/closest-subsequence-sum/
<CANT USE BITSETS HERE>

SOLUTIONS:
- Nearest Subset sum using Recursive DP-> TLE/MLE
- Cant use bitsets -> Negative numbers
Why? Because N is too large to keep in memory, so MEET IN THE MIDDLE

ALGO
1. Find all possible subset sums in left and right part
2. Iterate each sum in leftSums -> Check the best pair you can find with sums in right using Binary Search

"""
from typing import List
import bisect

class Solution:
    def getSums(self, nums: List[int], start: int, end: int) -> List[int]:
        n = end - start
        sums = []
        for mask in range(1 << n):  # enumerate all 2^n subsets
            s = 0
            for i in range(n):
                if mask & (1 << i):
                    s += nums[start + i]
            sums.append(s)
        return sums

    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        leftSums = self.getSums(nums, 0, n // 2)
        rightSums = self.getSums(nums, n // 2, n)
        rightSums.sort()

        result = float('inf')

        for s in leftSums:
            remaining = goal - s
            idx = bisect.bisect_left(rightSums, remaining)

            # Case 1: rem is smaller than all elements → only ceiling exists
            if idx == 0: result = min(result, abs(goal - (s + rightSums[0])))

            # Case 2: insertion strictly inside → both floor and ceiling exist
            if 0 < idx < len(rightSums):
                result = min(result, abs(goal - (s + rightSums[idx])))     # ceiling
                result = min(result, abs(goal - (s + rightSums[idx - 1]))) # floor

            # Case 3: rem is greater than all  → only floor exists
            if idx == len(rightSums): result = min(result, abs(goal - (s + rightSums[-1])))

            if result == 0: return 0
        
        return result


class RecursiveSol:
    def minimizeTheDifference(self, arr: List[int], target: int) -> int:
        n = len(arr)
        @lru_cache(maxsize=None)
        def solve(i, csum):
            if row == n:
                return abs(csum-target)
            
            return min(
                solve(i+1, csum),
                solve(i+1, csum+arr[i])
            )
        
        return solve(0,0)

