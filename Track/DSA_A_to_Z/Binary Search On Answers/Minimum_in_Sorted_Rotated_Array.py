"""
Problem:  Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

SOLUTION:
- Similar as Bin Search in Rotated Sorted array I, II
- Logic, for each mid you have two halves out of which one is definitely sorted
    - Check if arr[mid] is the minimum
    1. LEFT IS SORTED:  
        - check if arr[lo] is min (lowest of left subarray will be arr[lo] since its the first element in sorted arr)
        - Check right half now - lo=mid+1 (Min you can take in left half is already checked i.e arr[lo])
    2. RIGHT IS SORTED
        - check if arr[mid+1] is min (lowest of right subarray will be arr[mid+1] since its the first element in sorted arr)
        - Check left half now - hi=mid-1 (Min you can take in right half is already checked i.e arr[mid+1])
"""

class Solution:
    def findMin(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr)-1

        res = float("inf")
        while lo<=hi:
            mid = lo + (hi-lo)//2
            res = min(res, arr[mid])
            if arr[lo]<=arr[mid]: # LEFT part is sorted
                res = min(res, arr[lo]) # since its sorted lowest ele = arr[lo]
                lo = mid+1
            else:
                res = min(res, arr[mid+1])
                hi = mid-1
        
        return res
                


        