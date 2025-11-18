"""
https://leetcode.com/problems/minimum-size-subarray-sum/
"""
class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        n = len(arr)
        l,r = 0,0

        csum = 0
        res = float("inf")

        while r<n:
            csum += arr[r]
            if csum < target: # expand the window
                r += 1
            else:
                res = min(r-l+1, res)
                while l<=r and csum >= target: # start shrinking
                    res = min(r-l+1, res)
                    csum -= arr[l]
                    l += 1
   
                r += 1

        return 0 if res == float("inf") else res


"""
class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, 0
        csum = 0
        res = float("inf")

        while r < n:
            csum += arr[r]

            while csum >= target:
                res = min(res, r - l + 1)
                csum -= arr[l]
                l += 1

            r += 1

        return 0 if res == float("inf") else res

"""