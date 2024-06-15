"""
Problem: 
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75
- Given a binary array nums, you should delete one element from it.
- Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Solution: 
- https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/3719568/beat-s-100-c-java-python-beginner-friendly

- Question reduces to -> Find largest subarray containing atmost one 0 (because you will remove that and merge)

"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = 0
        res = 0
        left = 0

        for right, x in enumerate(nums):
            if x==0:
                zeros += 1

            # make sure you have at most 1 zero
            while zeros > 1: # in case n_zeros > 1 => increment left to find first zero
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        if res == n: # all are 1s, no zeros -> so left was never incremented
            return n-1
        else:
            return res-1
                

        