"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

class Solution:
    def first_occurence(self, arr, target):
        lo, hi = 0, len(arr)-1
        res = -1
        while lo<=hi:
            mid = lo+ (hi-lo)//2
            if arr[mid] == target:
                res = mid
                hi = mid-1
            elif arr[mid]>target:
                hi = mid-1
            else:
                lo = mid+1
        
        return res
    
    def last_occurence(self, arr, target):
        lo, hi = 0, len(arr)-1
        res = -1
        while lo<=hi:
            mid = lo+ (hi-lo)//2
            if arr[mid] == target:
                res = mid
                lo = mid+1
            elif arr[mid]>target:
                hi = mid-1
            else:
                lo = mid+1
        
        return res

    def searchRange(self, arr: List[int], target: int) -> List[int]:
        return [self.first_occurence(arr, target), self.last_occurence(arr, target)]

        