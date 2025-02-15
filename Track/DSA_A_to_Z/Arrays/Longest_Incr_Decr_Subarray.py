class Solution:
    def lis(self, nums):
        n = len(nums)
        res = 1
        
        l, r = 0, 0
        while r<n:
            if l==r: # same index -> just go to next
                r+=1
            elif nums[r]>nums[r-1]: # strictly increasing
                r+=1
            else: # new subarray starts here
                l=r
                r=l+1

            res = max(res, r-l)

        return res

             

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        print(self.lis(nums), self.lis(nums[::-1]))
        return max(self.lis(nums), self.lis(nums[::-1]))
        