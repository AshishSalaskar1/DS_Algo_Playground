"""
https://leetcode.com/problems/partition-equal-subset-sum/

ALGO
1. Check if you can make subset sum = total//2, by using any number of items

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def subsetsum(arr: list[int], target):
            n = len(arr)
            dp = [[False for _ in range(target+1)] for _ in range(n+1)]

            dp[0][0] = True

            for i in range(n+1):
                for j in range(target+1):
                    if i==0 and j==0:
                        dp[i][j] = True
                    elif j==0:
                        dp[i][j] = True
                    elif i==0:
                        dp[i][j] = False
                    elif arr[i-1]>j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            return dp

        n = len(nums)
        dp = subsetsum(nums, sum(nums))
        total = sum(nums);target=0

        if total%2 != 0: # odd sum -> cant split into 2
            return False
        else:
            target = total//2
        
        for row in range(0,n+1):
            if dp[row][target]:
                return True

        return False
        