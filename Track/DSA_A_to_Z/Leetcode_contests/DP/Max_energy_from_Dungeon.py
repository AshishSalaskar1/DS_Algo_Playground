"""
Link: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/

SOLUTION:
- You can only jump to i+k (only one jump -> so no max needed)
- You need to make atleast 1 jump (if possible) for answer 
- At each step you have 2 options
    1. jump = arr[i]+dp[i+k] if i+k<n
    2. dont jump = arr[i] (dont jump value will be same)
"""

class Solution:
    def maximumEnergy(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [arr[_] for _ in range(n)] # assume you dont jump and stay

        dp[n-1] = arr[n-1] # last ele -> cant jump
        for i in reversed(range(n-1)):
            if i+k < n: # jump possible
                dp[i] = arr[i]+dp[i+k]

        return max(dp)

        