"""
PROBLEM: Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

SOLUTION:
- Variation of PREFIX SUM PROBLEM

"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], target: int) -> int:
        hmap = {0:1} # IMPORTANT
        csum,res = 0,0
        for x in nums:
            csum += x
            if csum-target in hmap  or csum==target:
                res += hmap[csum-target]
            
            hmap[csum] = hmap.get(csum, 0) + 1
        
        return res


# 5 2  3  2
# 5 7 10 12

# [1,0,1,0,1]
