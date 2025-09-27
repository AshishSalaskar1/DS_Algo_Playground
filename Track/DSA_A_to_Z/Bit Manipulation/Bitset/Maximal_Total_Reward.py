"""
Maximal Total Reward: https://leetcode.com/problems/maximum-total-reward-using-operations-ii/description/


SOLUTION: Classic bitset
- What changes here from subset from?
    - There we add `x` to EVERY SET BIT (subset sum possible) on right: bitset |= bitset<<x
    - Here, you add `x` to every bit on right (whether set or not doesnt matter)
    - Why? If current reward `x` is greater than every thing on right, THEN YOU CAN ADD THOSE UP
"""
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        MAX_REWARD = 100001
        nums = sorted(rewardValues)
        n = len(nums)

        bitset = 1 # reward of 0 is always available
        for num in nums:
            # In normal subset sum => you want to add num to all on right 
            # Here, you want to make everything on right as set and then add num
            # why? if reward[x] is possible, then you can add any reward < x (everything on right)

            mask = (1<<num)-1 # set first num bits as 1
            bitset |= (bitset&mask) << num
        
        # First set bit
        return bitset.bit_length() - 1