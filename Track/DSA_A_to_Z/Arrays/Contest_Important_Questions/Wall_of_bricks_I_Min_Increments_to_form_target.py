"""
PROBLEM 1: https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/
PROBLEM 2: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array


WALL OF BRICKS: 
- You initially have array of zeros and you need to reach target by only increments 
    (You can only lay bricks in upward direction in subarray fashion)
- https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/solutions/754682/Wall-of-bricks/

WALL OF BRICKS II:
- You initially have array give and you need to reach target by increments or Decrements 
    (You can lay bricks in upward + downward direction in subarray fashion)
-https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/solutions/5509009/Really-Simple-Wall-of-Bricks-solution-(Python)/

"""

class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        res = target[0]
        for i in range(1,len(target)):
            if target[i]>target[i-1]:
                res += target[i]-target[i-1]
        
        return res