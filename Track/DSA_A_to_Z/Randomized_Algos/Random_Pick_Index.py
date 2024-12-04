"""
Problem: https://leetcode.com/problems/random-pick-index/submissions/1468326735/?envType=problem-list-v2&envId=randomized

Solution:
1. Store val: [list of indexes]
2. Apply Fischer-Yeates to each of such list of indexes
"""

from collections import defaultdict
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.revmap = defaultdict(list)

        for i, x in enumerate(self.nums):
            self.revmap[x].append(i)
        
        for val in self.revmap:
            indexes = self.revmap[val]
            if len(indexes) == 1:
                continue
            
            # random shuffling in those indexes
            for i in range(len(indexes)-1,0,-1):
                rint = random.randint(0,i)
                indexes[i], indexes[rint] = indexes[rint], indexes[i]
            
            self.revmap[val] = indexes
            
        

    def pick(self, target: int) -> int:
        indexes = self.revmap[target]

        if len(indexes) == 1:
            return indexes[0]
        
        return indexes[random.randint(0,len(indexes)-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)