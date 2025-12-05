"""
PROBLEM: https://leetcode.com/problems/partition-array-for-maximum-sum/
- Partition the array into (contiguous) subarrays of length at most k. 
- After partitioning, each subarray has their values changed to become the maximum value of that subarray.


SOLUTION: FRONT PARTITIONING
=> solve(start, k)
    - max res if you start partioning at i (before i)
    - You can at max make k partitions starting at i
    - for end: i -> i+k: # keep on storing length and max_ele to reduce TC
        - make sure end < n
        - res = length_of_cur_partition * max(cur_partition)
                + solve(start+1)
        - res = len * max_eleme + solve(start+1)


"""

from functools import cache
class Solution:
    @cache
    def solve(self, start, k):
        if start == self.n:
            return 0

        max_res = float("-inf")
        max_ele = float("-inf")
        part_length = 0
        for end in range(start, start+k):
            if end >= self.n:
                break
            part_length += 1
            max_ele = max(max_ele, self.arr[end])
            res = (part_length*max_ele) + self.solve(end+1, k)
            max_res = max(max_res, res)
        
        return max_res


    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.arr = arr
        self.n = len(arr)
        return self.solve(0, k)

    

        