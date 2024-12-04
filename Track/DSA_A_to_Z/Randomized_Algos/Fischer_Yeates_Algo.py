"""
Problem: https://leetcode.com/problems/shuffle-an-array/
s
Solution: https://youtu.be/4zx5bM2OcvA?si=tM9bL0Bp24gamWZm
"""

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.original = nums.copy()
        

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums
        

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n-1,0,-1):
            rint = random.randint(0,i)
            self.nums[i], self.nums[rint] = self.nums[rint], self.nums[i]
        
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()