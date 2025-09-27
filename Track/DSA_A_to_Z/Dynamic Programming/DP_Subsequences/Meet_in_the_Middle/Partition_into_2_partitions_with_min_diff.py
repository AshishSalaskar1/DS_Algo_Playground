"""
Partition Array Into Two Arrays to Minimize Sum Difference (https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/)


LOGIC
- Same as "Closest Subsequence Sum", but there we just need subset sums for left and right
- CHANGE HERE: <For each part you need all possible subsequence sums using 'k' elements>

WAYS
- sums_by_count() -> returns DICT<num_of_items_taken, SET(all_poss_subsequence_sums_using_k_items)

SOLUTION:
- get sums_by_count() for both left and right
1. Iterate through each `k` from left side
    - If you have taken `k` items from left, then take `n-k` items from right side
    - You will get all possible sums for `k` from left and `n-k` from left.
    - Try to find best match such that SUM(`k`)+SUM(`n-k`) = totalsum//2

"""
from typing import List
import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n2 = len(nums)
        n = n2 // 2
        left = nums[:n]
        right = nums[n:]
        total = sum(nums)

        # Returns a list sums_by_count where sums_by_count[k]
        # contains all subset sums using exactly k elements.
        def sums_by_count(arr: List[int]) -> List[List[int]]:
            m = len(arr)
            buckets = [[] for _ in range(m + 1)]
            # Enumerate all subsets of arr
            for mask in range(1 << m):
                csum = 0
                items_taken = 0
                i = 0
                while i < m:
                    if (mask >> i) & 1:
                        csum += arr[i]
                        items_taken += 1
                    i += 1
                buckets[items_taken].append(csum)
            return buckets

        sums_left = sums_by_count(left)    # List[List[int]] length n+1
        sums_right = sums_by_count(right)  # List[List[int]] length n+1

        # Sort each right bucket for binary search
        for k in range(n + 1):
            sums_right[k].sort()

        ans = float('inf')

        # We want to pick exactly n elements total: k from left, n-k from right
        half = total // 2  # integer target for search (we still compute exact diff)
        for k in range(n + 1):
            left_bucket = sums_left[k] # all possible subset sums taking 'k' elements from left
            right_bucket = sums_right[n - k] #  all possible subset sums taking 'n-k' elements from left
            # right_bucket is sorted

            for s in left_bucket:
                target = half - s
                idx = bisect.bisect_left(right_bucket, target)

                # Check candidate at idx (ceiling)
                if idx < len(right_bucket):
                    pick = s + right_bucket[idx]
                    diff = abs(total - 2 * pick)
                    if diff < ans:
                        ans = diff
                        if ans == 0:
                            return 0

                # Check candidate at idx-1 (floor)
                if idx - 1 >= 0:
                    pick = s + right_bucket[idx - 1]
                    diff = abs(total - 2 * pick)
                    if diff < ans:
                        ans = diff
                        if ans == 0:
                            return 0

        return ans
