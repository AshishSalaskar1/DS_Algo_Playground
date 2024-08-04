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



SOLUTION: (Here both refers to diffs[i-1], diffs[i])
- Both are +ve: add diff if increasing trend
- Both are -ve: add diff if increasing trend in reverse direction
- If mixed (-ve -> +ve OR +ve -> -ve) = abs(diffs[i])

Explaination for mixed:
1 2 -4 5 2
1 => 1
2 => 1+ (2-1) = 2

Now 2,-4 MIXED => 2+ abs(4)
- Why 4 got added?
Imagine you have laid 2 rows of bricks -> (first you one base: [1][1], then lay one more row only on 2:[1][1+1] = 1 2)
Now you lay 4 more rows in negative direction THATS WHY +4

5 => -4,5 = res+5
- You will just lay the bricks in the direction you want to pillar upon (older one cant be a surface since its in reverse direction)
"""
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        diffs = [y-x for x,y in zip(nums, target)]

        res = abs(diffs[0])
        for i in range(1,n):
            if diffs[i-1]>0 and diffs[i]>0: # POSITIVE TREND
                if diffs[i] > diffs[i-1]: # upward trend -> Downwards trend(no need, since its already laid out while upward)
                    res += diffs[i]-diffs[i-1]
            elif diffs[i-1]<0 and diffs[i]<0: # NEGATIVE TREND
                if abs(diffs[i]) > abs(diffs[i-1]): # downward increasing trend -> upwards increasing already taken care of
                    res += abs(diffs[i])-abs(diffs[i-1])
            else: # MIXED TREND
                res += abs(diffs[i]) # why diff only? You will start from base=0 first and then lay these in upward/downward direction
        return res
"""
1 -5 -2 4
"""