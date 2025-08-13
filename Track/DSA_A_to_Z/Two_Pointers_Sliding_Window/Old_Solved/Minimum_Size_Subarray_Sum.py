"""
PROBLEM: Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

SOLUTION :https://leetcode.com/problems/minimum-size-subarray-sum/solutions/5348515/python-sliding-window-and-binary-search-solutions
"""

class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 1 if arr[0] >= target else 0

        left,right = 0,0
        res = float("inf")
        csum = arr[0]

        while left<=right and right < n:
            if arr[left] >= target or arr[right] >= target:
                return 1
            
            if csum >= target:
                res = min(res, right-left+1)
                csum -= arr[left] # first decreement and then decrease right
                left += 1
            
            else: # csum < target
                right += 1
                if right >= n:
                    break
                csum += arr[right]
        
        return res if res!=float("inf") else 0

            

            

            



        